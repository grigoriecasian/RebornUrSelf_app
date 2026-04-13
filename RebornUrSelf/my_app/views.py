import csv
import json
from datetime import date, timedelta

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.db.models import Sum

from django.views.decorators.http import require_POST
from django.utils import timezone

from .models import (
    Diet, Recipe, Workout, MealImage, VipPayment,
    UserProfile, DailyLog, ChatMessage, WeightEntry,
    Citat, Reteta, Exercitiu, ProgramZilnic, DailyCheckIn,
    Notification, Achievement, UserAchievement,
)
from .forms import (
    RegisterForm, UserProfileForm, MealImageForm,
    InsulinQuestionnaireForm, AICompanionForm,
    DailyLogForm, WeightEntryForm, DailyCheckInForm,
)
from .ai_utils import (
    estimate_calories_from_image, chat_with_ai,
    generate_meal_plan,
)


@login_required
def home(request):
    today = date.today()
    profile = request.user.userprofile

    if request.method == 'POST' and 'update_profile' in request.POST:
        profile_form = UserProfileForm(request.POST, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profil actualizat!')
            return redirect('home')
    else:
        profile_form = UserProfileForm(instance=profile)

    checkin, _ = DailyCheckIn.objects.get_or_create(
        user=request.user, date=today
    )
    if request.method == 'POST' and 'checkin' in request.POST:
        checkin_form = DailyCheckInForm(request.POST, instance=checkin)
        if checkin_form.is_valid():
            checkin_form.save()
            messages.success(request, f'Check-in salvat! Scor: {checkin.score}/100')
            return redirect('home')
    else:
        checkin_form = DailyCheckInForm(instance=checkin)

    week_scores = []
    day_names = ['Lun', 'Mar', 'Mie', 'Joi', 'Vin', 'Sam', 'Dum']
    for i in range(6, -1, -1):
        d = today - timedelta(days=i)
        try:
            ci = DailyCheckIn.objects.get(user=request.user, date=d)
            week_scores.append({'day': day_names[d.weekday()], 'score': ci.score, 'date': d.strftime('%d/%m')})
        except DailyCheckIn.DoesNotExist:
            week_scores.append({'day': day_names[d.weekday()], 'score': 0, 'date': d.strftime('%d/%m')})

    logs_azi = DailyLog.objects.filter(user=request.user, date=today)
    total_azi = logs_azi.aggregate(total=Sum('calories'))['total'] or 0

    week_start = today - timedelta(days=6)
    week_checkins = DailyCheckIn.objects.filter(user=request.user, date__gte=week_start)
    avg_score = 0
    if week_checkins.exists():
        avg_score = int(sum(c.score for c in week_checkins) / week_checkins.count())

    check_achievements(request.user)
    generate_notifications(request.user)

    earned_badges = list(UserAchievement.objects.filter(
        user=request.user
    ).select_related('achievement').order_by('-earned_at')[:5])
    for eb in earned_badges:
        eb.css_color = COLOR_MAP.get(eb.achievement.color, '#94a3b8')

    ctx = {
        'profile': profile,
        'profile_form': profile_form,
        'checkin_form': checkin_form,
        'checkin': checkin,
        'today_score': checkin.score,
        'avg_score': avg_score,
        'week_scores': json.dumps(week_scores),
        'calories_today': total_azi,
        'today': today,
        'earned_badges': earned_badges,
    }
    return render(request, 'wellness/home.html', ctx)


def landing_page(request):
    if request.user.is_authenticated:
        return redirect('home')

    citate = Citat.objects.all()
    retete = Reteta.objects.all()
    exercitii = Exercitiu.objects.all()
    programe = ProgramZilnic.objects.all()

    citate_dict = {}
    for c in citate:
        citate_dict[c.tip] = c.text

    programe_list = []
    for p in programe:
        programe_list.append({
            'tip_dieta': p.tip_dieta,
            'zi': p.zi,
            'trezire': p.trezire,
            'mic_dejun_ora': p.mic_dejun_ora,
            'gustare1_ora': p.gustare1_ora,
            'antrenament_ora': p.antrenament_ora,
            'antrenament_tip': p.antrenament_tip,
            'pranz_ora': p.pranz_ora,
            'gustare2_ora': p.gustare2_ora,
            'cina_ora': p.cina_ora,
            'relaxare_ora': p.relaxare_ora,
            'somn_ora': p.somn_ora,
            'ore_somn': p.ore_somn,
            'sfat_somn': p.sfat_somn,
            'sfat_zi': p.sfat_zi,
        })

    return render(request, 'wellness/index.html', {
        'retete_db': retete,
        'exercitii_db': exercitii,
        'citate_db': json.dumps(citate_dict),
        'programe_db': json.dumps(programe_list),
    })


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            messages.success(request, 'Cont creat! Bine ai venit.')
            return redirect('profile')
    else:
        form = RegisterForm()
    return render(request, 'wellness/register.html', {'form': form})


@login_required
def profile_view(request):
    profile = request.user.userprofile
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profil actualizat.')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile)

    weight_history = WeightEntry.objects.filter(user=request.user)[:10]

    return render(request, 'wellness/profile.html', {
        'form': form,
        'profile': profile,
        'weight_history': weight_history,
    })


def diet_list(request):
    goal = request.GET.get('goal')
    diets = Diet.objects.all()
    if goal in ['lose', 'maintain', 'gain']:
        diets = diets.filter(goal=goal)
    return render(request, 'wellness/diet_list.html', {
        'diets': diets,
        'selected_goal': goal,
    })


def diet_detail(request, diet_id):
    diet = get_object_or_404(Diet, id=diet_id)
    recipes = diet.recipes.all()

    days = []
    day_names = {1: 'Luni', 2: 'Marti', 3: 'Miercuri', 4: 'Joi', 5: 'Vineri', 6: 'Sambata', 7: 'Duminica'}
    meal_order = ['breakfast', 'lunch', 'dinner', 'snack']

    for day_num in range(1, 8):
        day_recipes = recipes.filter(day=day_num)
        if day_recipes.exists():
            meals = []
            for mt in meal_order:
                meal_qs = day_recipes.filter(meal_type=mt)
                if meal_qs.exists():
                    meals.append({
                        'type': mt,
                        'label': meal_qs.first().get_meal_type_display(),
                        'recipes': meal_qs,
                    })
            days.append({
                'number': day_num,
                'name': day_names[day_num],
                'meals': meals,
                'total_cal': sum(r.calories for r in day_recipes),
            })

    return render(request, 'wellness/diet_detail.html', {
        'diet': diet,
        'recipes': recipes,
        'days': days,
    })


def recipe_list(request, diet_id=None):
    if diet_id:
        diet = get_object_or_404(Diet, id=diet_id)
        recipes = diet.recipes.all()
    else:
        diet = None
        recipes = Recipe.objects.all()
    return render(request, 'wellness/recipe_list.html', {
        'diet': diet,
        'recipes': recipes,
    })


def workout_list(request):
    env = request.GET.get('environment')
    diff = request.GET.get('difficulty')
    workouts = Workout.objects.all()
    if env in ['home', 'gym', 'outdoor']:
        workouts = workouts.filter(environment=env)
    if diff in ['easy', 'medium', 'hard']:
        workouts = workouts.filter(difficulty=diff)
    return render(request, 'wellness/workout_list.html', {
        'workouts': workouts,
        'selected_env': env,
        'selected_diff': diff,
    })


def workout_detail(request, workout_id):
    workout = get_object_or_404(Workout, id=workout_id)
    return render(request, 'wellness/workout_detail.html', {'workout': workout})


@login_required
def ai_calories_view(request):
    estimated = None
    result_data = None

    if request.method == 'POST':
        form = MealImageForm(request.POST, request.FILES)
        if form.is_valid():
            meal = form.save(commit=False)
            meal.user = request.user
            meal.save()

            result_data = estimate_calories_from_image(meal.image.path)

            meal.estimated_calories = result_data['calories']
            meal.comment = result_data['description']
            meal.save()

            estimated = result_data['calories']
            messages.success(request, f'Estimare: ~{estimated} kcal')
    else:
        form = MealImageForm()

    history = MealImage.objects.filter(user=request.user).order_by('-created_at')[:10]

    return render(request, 'wellness/ai_calories.html', {
        'form': form,
        'estimated': estimated,
        'result_data': result_data,
        'history': history,
    })


@login_required
def vip_subscribe(request):
    profile = request.user.userprofile
    if request.method == 'POST':
        VipPayment.objects.create(user=request.user, amount_eur=100, is_active=True)
        profile.is_vip = True
        profile.save()
        messages.success(request, 'Felicitari! Ai devenit VIP.')
        return redirect('profile')
    return render(request, 'wellness/vip_subscribe.html', {
        'profile': profile,
    })


def insulin_info_view(request):
    result = None
    explanation = None
    recommendations = None

    if request.method == 'POST':
        form = InsulinQuestionnaireForm(request.POST)
        if form.is_valid():
            score = sum(1 for v in form.cleaned_data.values() if v)

            if score >= 4:
                result = 'RISC CRESCUT'
                explanation = (
                    'Ai mai multe semne asociate cu rezistenta la insulina. '
                    'Nu este un diagnostic, dar e important sa discuti cu medicul '
                    'si sa faci analize (glicemie, insulina bazala, HOMA-IR).'
                )
                recommendations = [
                    'Programeaza-te la medic pentru analize de sange',
                    'Elimina zaharul rafinat si alimentele ultraprocesate',
                    'Miscare zilnica - minim 30 minute mers pe jos',
                    'Dieta cu indice glicemic scazut',
                    'Somn 7-8 ore pe noapte',
                ]
            elif score >= 2:
                result = 'RISC MODERAT'
                explanation = (
                    'Exista cateva indicii. Monitizeaza-ti stilul de viata '
                    'si discuta cu medicul la controlul periodic.'
                )
                recommendations = [
                    'Reducerea carbohidratilor simpli',
                    'Activitate fizica regulata (3-4 zile/sapt)',
                    'Control medical anual cu analize de sange',
                ]
            else:
                result = 'RISC SCAZUT'
                explanation = (
                    'Riscul pare mic, dar mentine o alimentatie echilibrata '
                    'si miscare regulata pentru prevenire.'
                )
                recommendations = [
                    'Mentine un stil de viata activ',
                    'Alimentatie variata si echilibrata',
                    'Control medical periodic',
                ]

            if request.user.is_authenticated:
                profile = request.user.userprofile
                profile.suspected_insulin_resistance = (score >= 2)
                profile.save()
    else:
        form = InsulinQuestionnaireForm()

    return render(request, 'wellness/insulin_info.html', {
        'form': form,
        'result': result,
        'explanation': explanation,
        'recommendations': recommendations,
    })


@login_required
def ai_companion_view(request):
    profile = request.user.userprofile

    if not profile.is_vip:
        messages.warning(request, 'Chatbot-ul AI e disponibil doar pentru utilizatorii VIP.')
        return redirect('vip_subscribe')

    response_text = None
    if request.method == 'POST':
        form = AICompanionForm(request.POST)
        if form.is_valid():
            msg = form.cleaned_data['message']

            ChatMessage.objects.create(
                user=request.user,
                role='user',
                content=msg
            )

            history = list(
                ChatMessage.objects.filter(user=request.user)
                .order_by('-created_at')[:20]
                .values('role', 'content')
            )
            history.reverse()

            response_text = chat_with_ai(msg, history=history, user_profile=profile)

            ChatMessage.objects.create(
                user=request.user,
                role='assistant',
                content=response_text
            )
    else:
        form = AICompanionForm()

    chat_history = list(
        ChatMessage.objects.filter(user=request.user).order_by('-created_at')[:30]
    )
    chat_history.reverse()

    return render(request, 'wellness/ai_companion.html', {
        'form': form,
        'response': response_text,
        'chat_history': chat_history,
    })


@login_required
def dashboard_view(request):
    today = date.today()
    profile = request.user.userprofile

    logs_today = DailyLog.objects.filter(user=request.user, date=today)
    totals = logs_today.aggregate(
        cal=Sum('calories'),
        prot=Sum('protein'),
        carb=Sum('carbs'),
        fat_total=Sum('fat'),
    )

    if profile.weight_kg:
        if profile.goal == 'lose':
            target_cal = int(profile.weight_kg * 25)
        elif profile.goal == 'gain':
            target_cal = int(profile.weight_kg * 35)
        else:
            target_cal = int(profile.weight_kg * 30)
    else:
        target_cal = 2000

    week_start = today - timedelta(days=6)
    weekly_data = []
    for i in range(7):
        d = week_start + timedelta(days=i)
        day_cal = DailyLog.objects.filter(
            user=request.user, date=d
        ).aggregate(total=Sum('calories'))['total'] or 0
        weekly_data.append({
            'date': d.strftime('%d/%m'),
            'day_name': ['Lun', 'Mar', 'Mie', 'Joi', 'Vin', 'Sam', 'Dum'][d.weekday()],
            'calories': day_cal,
        })

    cal_consumed = totals['cal'] or 0
    remaining = max(target_cal - cal_consumed, 0)

    return render(request, 'wellness/dashboard.html', {
        'logs_today': logs_today,
        'total_cal': cal_consumed,
        'total_protein': round(totals['prot'] or 0, 1),
        'total_carbs': round(totals['carb'] or 0, 1),
        'total_fat': round(totals['fat_total'] or 0, 1),
        'target_cal': target_cal,
        'remaining_cal': remaining,
        'weekly_data': json.dumps(weekly_data),
        'profile': profile,
        'today': today,
    })


@login_required
def add_food_log(request):
    if request.method == 'POST':
        form = DailyLogForm(request.POST)
        if form.is_valid():
            log = form.save(commit=False)
            log.user = request.user
            if not log.date:
                log.date = date.today()
            log.save()
            messages.success(request, f'{log.food_name} adaugat ({log.calories} kcal)')
            return redirect('dashboard')
    else:
        form = DailyLogForm(initial={'date': date.today()})
    return render(request, 'wellness/add_food.html', {'form': form})


@login_required
def delete_food_log(request, log_id):
    log = get_object_or_404(DailyLog, id=log_id, user=request.user)
    if request.method == 'POST':
        log.delete()
        messages.info(request, 'Intrare stearsa.')
    return redirect('dashboard')


@login_required
def progress_view(request):
    profile = request.user.userprofile

    if request.method == 'POST':
        form = WeightEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            profile.weight_kg = entry.weight
            profile.save()
            messages.success(request, f'Greutate inregistrata: {entry.weight} kg')
            return redirect('progress')
    else:
        form = WeightEntryForm(initial={'date': date.today()})

    today = date.today()
    entries = WeightEntry.objects.filter(user=request.user)[:30]
    chart_data = list(
        WeightEntry.objects.filter(user=request.user)
        .order_by('date')
        .values('date', 'weight')[:30]
    )
    for item in chart_data:
        item['date'] = item['date'].strftime('%d/%m')

    calorie_chart = []
    for i in range(13, -1, -1):
        d = today - timedelta(days=i)
        day_cal = DailyLog.objects.filter(
            user=request.user, date=d
        ).aggregate(total=Sum('calories'))['total'] or 0
        calorie_chart.append({
            'date': d.strftime('%d/%m'),
            'calories': day_cal,
        })

    checkin_chart = []
    for i in range(13, -1, -1):
        d = today - timedelta(days=i)
        try:
            ci = DailyCheckIn.objects.get(user=request.user, date=d)
            checkin_chart.append({'date': d.strftime('%d/%m'), 'score': ci.score})
        except DailyCheckIn.DoesNotExist:
            checkin_chart.append({'date': d.strftime('%d/%m'), 'score': 0})

    this_week_start = today - timedelta(days=6)
    last_week_start = today - timedelta(days=13)
    last_week_end = today - timedelta(days=7)

    this_week_cal = DailyLog.objects.filter(
        user=request.user, date__gte=this_week_start
    ).aggregate(total=Sum('calories'))['total'] or 0
    last_week_cal = DailyLog.objects.filter(
        user=request.user, date__gte=last_week_start, date__lte=last_week_end
    ).aggregate(total=Sum('calories'))['total'] or 0
    avg_cal_this = round(this_week_cal / 7)
    avg_cal_last = round(last_week_cal / 7)

    this_week_checkins = DailyCheckIn.objects.filter(user=request.user, date__gte=this_week_start)
    last_week_checkins = DailyCheckIn.objects.filter(user=request.user, date__gte=last_week_start, date__lte=last_week_end)
    avg_score_this = int(sum(c.score for c in this_week_checkins) / max(this_week_checkins.count(), 1))
    avg_score_last = int(sum(c.score for c in last_week_checkins) / max(last_week_checkins.count(), 1))

    weight_this = WeightEntry.objects.filter(user=request.user, date__gte=this_week_start).order_by('-date').first()
    weight_last = WeightEntry.objects.filter(user=request.user, date__gte=last_week_start, date__lte=last_week_end).order_by('-date').first()

    if profile.weight_kg:
        if profile.goal == 'lose':
            target_cal = int(profile.weight_kg * 25)
        elif profile.goal == 'gain':
            target_cal = int(profile.weight_kg * 35)
        else:
            target_cal = int(profile.weight_kg * 30)
    else:
        target_cal = 2000

    return render(request, 'wellness/progress.html', {
        'form': form,
        'entries': entries,
        'chart_data': json.dumps(chart_data),
        'calorie_chart': json.dumps(calorie_chart),
        'checkin_chart': json.dumps(checkin_chart),
        'target_cal': target_cal,
        'avg_cal_this': avg_cal_this,
        'avg_cal_last': avg_cal_last,
        'avg_score_this': avg_score_this,
        'avg_score_last': avg_score_last,
        'weight_this': weight_this.weight if weight_this else None,
        'weight_last': weight_last.weight if weight_last else None,
        'cal_diff': avg_cal_this - avg_cal_last,
        'score_diff': avg_score_this - avg_score_last,
        'profile': profile,
    })


@login_required
def generate_plan_view(request):
    profile = request.user.userprofile
    if not profile.is_vip:
        messages.warning(request, 'Generarea de planuri e disponibila doar pt VIP.')
        return redirect('vip_subscribe')

    meals = generate_meal_plan(profile)
    total_cal = sum(m.get('calories', 0) for m in meals)

    return render(request, 'wellness/meal_plan.html', {
        'meals': meals,
        'total_cal': total_cal,
        'profile': profile,
    })


@login_required
def clear_chat(request):
    if request.method == 'POST':
        ChatMessage.objects.filter(user=request.user).delete()
        messages.info(request, 'Istoricul conversatiei a fost sters.')
    return redirect('ai_companion')


def check_achievements(user):
    from datetime import date, timedelta
    earned_ids = set(UserAchievement.objects.filter(user=user).values_list('achievement_id', flat=True))

    checkin_count = DailyCheckIn.objects.filter(user=user).count()
    meals_count = DailyLog.objects.filter(user=user).count()
    weight_count = WeightEntry.objects.filter(user=user).count()
    scans_count = MealImage.objects.filter(user=user).count()
    days_active = DailyCheckIn.objects.filter(user=user).values('date').distinct().count()

    today = date.today()
    streak = 0
    d = today
    while True:
        if DailyCheckIn.objects.filter(user=user, date=d).exists():
            streak += 1
            d -= timedelta(days=1)
        else:
            break

    stats = {
        'checkin_streak': streak,
        'meals_logged': meals_count,
        'weight_logged': weight_count,
        'scans_done': scans_count,
        'days_active': days_active,
    }

    for ach in Achievement.objects.all():
        if ach.id in earned_ids:
            continue
        val = stats.get(ach.condition_type, 0)
        if val >= ach.condition_value:
            UserAchievement.objects.create(user=user, achievement=ach)
            Notification.objects.create(
                user=user,
                message=f'Ai deblocat achievement-ul "{ach.name}"!',
                icon=ach.icon,
                type='success',
            )


def generate_notifications(user):
    today = date.today()
    today_notifs = Notification.objects.filter(user=user, created_at__date=today)

    if not DailyCheckIn.objects.filter(user=user, date=today, followed_diet=True).exists():
        if not today_notifs.filter(message__icontains='check-in').exists():
            Notification.objects.create(
                user=user,
                message='Nu ai completat check-in-ul de azi!',
                icon='fa-clipboard-check',
                type='warning',
            )

    if not DailyLog.objects.filter(user=user, date=today).exists():
        if not today_notifs.filter(message__icontains='aliment').exists():
            Notification.objects.create(
                user=user,
                message='Nu ai inregistrat niciun aliment azi. Adauga ce ai mancat!',
                icon='fa-utensils',
                type='info',
            )

    streak = 0
    d = today
    while DailyCheckIn.objects.filter(user=user, date=d).exists():
        streak += 1
        d -= timedelta(days=1)
    if streak >= 3 and not today_notifs.filter(message__icontains='serie').exists():
        Notification.objects.create(
            user=user,
            message=f'Ai o serie de {streak} zile consecutive! Continua asa!',
            icon='fa-fire',
            type='success',
        )


@login_required
@require_POST
def mark_notification_read(request, notif_id):
    notif = get_object_or_404(Notification, id=notif_id, user=request.user)
    notif.is_read = True
    notif.save()
    return JsonResponse({'ok': True})


@login_required
@require_POST
def dismiss_all_notifications(request):
    Notification.objects.filter(user=request.user, is_read=False).update(is_read=True)
    return JsonResponse({'ok': True})


COLOR_MAP = {
    'emerald': '#34d399', 'orange': '#fb923c', 'yellow': '#facc15',
    'blue': '#60a5fa', 'purple': '#a78bfa', 'teal': '#2dd4bf',
    'indigo': '#818cf8', 'amber': '#fbbf24', 'pink': '#f472b6',
    'rose': '#fb7185', 'red': '#f87171', 'green': '#4ade80',
}


@login_required
def achievements_view(request):
    all_achievements = Achievement.objects.all()
    earned = set(UserAchievement.objects.filter(user=request.user).values_list('achievement_id', flat=True))
    earned_list = UserAchievement.objects.filter(user=request.user).select_related('achievement').order_by('-earned_at')

    achievements_data = []
    for a in all_achievements:
        achievements_data.append({
            'achievement': a,
            'earned': a.id in earned,
            'css_color': COLOR_MAP.get(a.color, '#94a3b8'),
        })

    earned_with_colors = []
    for ua in earned_list:
        ua.css_color = COLOR_MAP.get(ua.achievement.color, '#94a3b8')
        earned_with_colors.append(ua)

    return render(request, 'wellness/achievements.html', {
        'achievements_data': achievements_data,
        'earned_list': earned_with_colors,
        'total': all_achievements.count(),
        'earned_count': len(earned),
    })


@login_required
def export_page(request):
    return render(request, 'wellness/export.html')


@login_required
def export_csv(request):
    today = date.today()
    start_date = today - timedelta(days=29)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="progres_rebornurself_{today.strftime("%Y%m%d")}.csv"'
    response.write('\ufeff')

    writer = csv.writer(response)
    writer.writerow(['Data', 'Greutate(kg)', 'Calorii consumate', 'Scor check-in', 'Observatii'])

    for i in range(30):
        d = start_date + timedelta(days=i)

        weight_entry = WeightEntry.objects.filter(user=request.user, date=d).first()
        weight_val = weight_entry.weight if weight_entry else ''
        note = weight_entry.note if weight_entry and weight_entry.note else ''

        day_cal = DailyLog.objects.filter(
            user=request.user, date=d
        ).aggregate(total=Sum('calories'))['total'] or ''

        try:
            ci = DailyCheckIn.objects.get(user=request.user, date=d)
            score = ci.score
        except DailyCheckIn.DoesNotExist:
            score = ''

        writer.writerow([d.strftime('%d/%m/%Y'), weight_val, day_cal, score, note])

    return response


@login_required
def export_print(request):
    today = date.today()
    start_date = today - timedelta(days=29)
    profile = request.user.userprofile

    weight_data = list(
        WeightEntry.objects.filter(user=request.user, date__gte=start_date)
        .order_by('date')
        .values('date', 'weight', 'note')
    )

    calorie_data = []
    for i in range(30):
        d = start_date + timedelta(days=i)
        totals = DailyLog.objects.filter(
            user=request.user, date=d
        ).aggregate(
            cal=Sum('calories'),
            prot=Sum('protein'),
            carb=Sum('carbs'),
            fat_total=Sum('fat'),
        )
        if totals['cal']:
            calorie_data.append({
                'date': d,
                'calories': totals['cal'] or 0,
                'protein': round(totals['prot'] or 0, 1),
                'carbs': round(totals['carb'] or 0, 1),
                'fat': round(totals['fat_total'] or 0, 1),
            })

    checkins = DailyCheckIn.objects.filter(
        user=request.user, date__gte=start_date
    ).order_by('date')

    return render(request, 'wellness/progress_print.html', {
        'profile': profile,
        'weight_data': weight_data,
        'calorie_data': calorie_data,
        'checkins': checkins,
        'start_date': start_date,
        'end_date': today,
    })
