from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    GOAL_CHOICES = [
        ('lose', 'Slăbire'),
        ('maintain', 'Menținere'),
        ('gain', 'Îngrășare'),
    ]
    GENDER_CHOICES = [
        ('M', 'Masculin'),
        ('F', 'Feminin'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    goal = models.CharField(max_length=20, choices=GOAL_CHOICES, default='maintain')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, default='')
    is_vip = models.BooleanField(default=False)
    has_insulin_resistance = models.BooleanField(default=False)
    suspected_insulin_resistance = models.BooleanField(default=False)
    weight_kg = models.FloatField(null=True, blank=True)
    height_cm = models.FloatField(null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f'Profil {self.user.username}'

    @property
    def bmi(self):
        if self.weight_kg and self.height_cm:
            h = self.height_cm / 100
            return round(self.weight_kg / (h * h), 1)
        return None


class Diet(models.Model):
    GOAL_CHOICES = UserProfile.GOAL_CHOICES

    name = models.CharField(max_length=100)
    goal = models.CharField(max_length=20, choices=GOAL_CHOICES)
    description = models.TextField()
    calories_per_day = models.IntegerField()
    is_insulin_friendly = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} ({self.get_goal_display()})'


class Recipe(models.Model):
    MEAL_TYPE_CHOICES = [
        ('breakfast', 'Mic dejun'),
        ('lunch', 'Prânz'),
        ('dinner', 'Cină'),
        ('snack', 'Gustare'),
    ]
    DAY_CHOICES = [
        (1, 'Luni'), (2, 'Marți'), (3, 'Miercuri'),
        (4, 'Joi'), (5, 'Vineri'), (6, 'Sâmbătă'), (7, 'Duminică'),
    ]

    diet = models.ForeignKey(Diet, related_name='recipes', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    calories = models.IntegerField()
    day = models.IntegerField(choices=DAY_CHOICES, default=1)
    meal_type = models.CharField(max_length=20, choices=MEAL_TYPE_CHOICES, default='lunch')
    image_url = models.URLField(blank=True, help_text='URL imagine reprezentativa')

    class Meta:
        ordering = ['day', 'meal_type']

    def __str__(self):
        return f'{self.get_day_display()} - {self.get_meal_type_display()} - {self.title}'


class Workout(models.Model):
    ENV_CHOICES = [
        ('home', 'Acasă'),
        ('gym', 'Sală'),
        ('outdoor', 'Afară'),
    ]
    DIFFICULTY_CHOICES = [
        ('easy', 'Începător'),
        ('medium', 'Intermediar'),
        ('hard', 'Avansat'),
    ]

    title = models.CharField(max_length=150)
    short_description = models.CharField(max_length=255)
    environment = models.CharField(max_length=20, choices=ENV_CHOICES)
    youtube_url = models.URLField(blank=True)
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES)
    duration_minutes = models.PositiveIntegerField()
    goal = models.CharField(
        max_length=20,
        choices=UserProfile.GOAL_CHOICES,
        default='maintain'
    )
    image_url = models.URLField(blank=True, help_text='URL imagine reprezentativa')

    def __str__(self):
        return self.title


class MealImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='meals/')
    estimated_calories = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'Meal {self.id} by {self.user.username}'


class VipPayment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    amount_eur = models.DecimalField(max_digits=6, decimal_places=2, default=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'VIP {self.user.username} - {self.amount_eur} EUR'


class DailyLog(models.Model):
    MEAL_TYPES = [
        ('breakfast', 'Mic dejun'),
        ('lunch', 'Prânz'),
        ('dinner', 'Cină'),
        ('snack', 'Gustare'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='daily_logs')
    date = models.DateField()
    meal_type = models.CharField(max_length=20, choices=MEAL_TYPES)
    food_name = models.CharField(max_length=200)
    calories = models.IntegerField()
    protein = models.FloatField(default=0)
    carbs = models.FloatField(default=0)
    fat = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date', 'meal_type']

    def __str__(self):
        return f'{self.food_name} - {self.calories} kcal ({self.user.username})'


class ChatMessage(models.Model):
    ROLE_CHOICES = [
        ('user', 'Utilizator'),
        ('assistant', 'Asistent'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_messages')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        preview = self.content[:50]
        return f'[{self.role}] {preview}'


class WeightEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='weight_entries')
    weight = models.FloatField()
    date = models.DateField()
    note = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ['-date']
        unique_together = ['user', 'date']

    def __str__(self):
        return f'{self.weight} kg - {self.date}'


class Citat(models.Model):
    tip = models.CharField(max_length=30)
    text = models.TextField()

    def __str__(self):
        return self.text[:60]


class Reteta(models.Model):
    nume = models.CharField(max_length=150)
    tip = models.CharField(max_length=30)  # slabit / mentinere / ingrasare
    masa = models.CharField(max_length=30)  # mic_dejun / gustare_1 / pranz / gustare_2 / cina
    zi = models.IntegerField()  # 1-7
    kcal = models.IntegerField()
    img_url_placeholder = models.CharField(max_length=200, blank=True)
    img_url = models.URLField(max_length=500, blank=True)
    instructiuni = models.TextField(blank=True)
    proteine = models.IntegerField(default=0)
    carbohidrati = models.IntegerField(default=0)
    grasimi = models.IntegerField(default=0)

    def __str__(self):
        return self.nume


class Exercitiu(models.Model):
    titlu = models.CharField(max_length=150)
    locatie = models.CharField(max_length=30)  # acasa / sala / aer_liber
    obiectiv = models.CharField(max_length=30)  # slabit / mentinere / ingrasare
    zi = models.IntegerField(default=0)  # 0=general, 1-7=ziua specifica
    descriere = models.TextField()
    tag = models.CharField(max_length=100)
    img_url = models.URLField(max_length=500, blank=True)
    youtube_url = models.URLField(max_length=300, blank=True)
    durata_minute = models.IntegerField(default=30)

    def __str__(self):
        return self.titlu


class ProgramZilnic(models.Model):
    tip_dieta = models.CharField(max_length=30)  # slabit / mentinere / ingrasare
    zi = models.IntegerField()  # 1-7
    trezire = models.CharField(max_length=10)
    mic_dejun_ora = models.CharField(max_length=10)
    gustare1_ora = models.CharField(max_length=10)
    antrenament_ora = models.CharField(max_length=10)
    antrenament_tip = models.CharField(max_length=100)
    pranz_ora = models.CharField(max_length=10)
    gustare2_ora = models.CharField(max_length=10)
    cina_ora = models.CharField(max_length=10)
    relaxare_ora = models.CharField(max_length=10)
    somn_ora = models.CharField(max_length=10)
    ore_somn = models.FloatField(default=8)
    sfat_somn = models.CharField(max_length=300, blank=True)
    sfat_zi = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return f'{self.tip_dieta} - Ziua {self.zi}'


class DailyCheckIn(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='checkins')
    date = models.DateField()
    followed_diet = models.BooleanField(default=False)
    followed_workout = models.BooleanField(default=False)
    followed_sleep = models.BooleanField(default=False)
    drank_water = models.BooleanField(default=False)
    no_junk_food = models.BooleanField(default=False)

    @property
    def score(self):
        checks = [
            self.followed_diet,
            self.followed_workout,
            self.followed_sleep,
            self.drank_water,
            self.no_junk_food,
        ]
        return int(sum(checks) / len(checks) * 100)

    class Meta:
        unique_together = ['user', 'date']
        ordering = ['-date']

    def __str__(self):
        return f'{self.user.username} - {self.date} - {self.score}pts'


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.CharField(max_length=300)
    icon = models.CharField(max_length=50, default='fa-bell')
    type = models.CharField(max_length=20, choices=[('info', 'Info'), ('success', 'Success'), ('warning', 'Warning')], default='info')
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.user.username} - {self.message[:50]}'


class Achievement(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    icon = models.CharField(max_length=50)
    color = models.CharField(max_length=20, default='emerald')
    condition_type = models.CharField(max_length=50)
    condition_value = models.IntegerField()

    def __str__(self):
        return self.name


class UserAchievement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='achievements')
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    earned_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'achievement']

    def __str__(self):
        return f'{self.user.username} - {self.achievement.name}'
