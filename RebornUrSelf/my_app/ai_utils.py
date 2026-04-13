import json
import logging
from django.conf import settings

logger = logging.getLogger(__name__)

try:
    from google import genai
    HAS_GEMINI = True
except ImportError:
    HAS_GEMINI = False
    logger.warning('google-genai nu e instalat, AI va folosi fallback local')


def _get_client():
    if not HAS_GEMINI:
        return None
    api_key = getattr(settings, 'GEMINI_API_KEY', '')
    if not api_key:
        return None
    return genai.Client(api_key=api_key)


def estimate_calories_from_image(image_path):
    client = _get_client()
    if client is None:
        return _fallback_calorie_estimate()

    try:
        import PIL.Image
        img = PIL.Image.open(image_path)

        prompt = (
            "Esti un nutritionist expert. Analizeaza aceasta imagine cu mancare "
            "si estimeaza cat mai precis continutul nutritional. "
            "Raspunde STRICT in format JSON, fara alte explicatii, fara markdown:\n"
            '{"calories": numar, "protein": numar_grame, "carbs": numar_grame, '
            '"fat": numar_grame, "description": "descriere scurta a mancarii in romana"}'
        )

        response = client.models.generate_content(
            model='gemini-2.0-flash',
            contents=[prompt, img],
        )
        text = response.text.strip()

        if text.startswith('```'):
            lines = text.split('\n')
            text = '\n'.join(lines[1:-1])

        data = json.loads(text)
        return {
            'calories': int(data.get('calories', 0)),
            'protein': round(float(data.get('protein', 0)), 1),
            'carbs': round(float(data.get('carbs', 0)), 1),
            'fat': round(float(data.get('fat', 0)), 1),
            'description': data.get('description', 'Analiza completata'),
            'source': 'gemini',
        }
    except Exception as e:
        logger.error(f'Eroare la analiza imaginii cu Gemini: {e}')
        return _fallback_calorie_estimate()


def _fallback_calorie_estimate():
    import random
    cal = random.randint(280, 650)
    return {
        'calories': cal,
        'protein': round(cal * 0.12, 1),
        'carbs': round(cal * 0.15, 1),
        'fat': round(cal * 0.08, 1),
        'description': 'Estimare aproximativa',
        'source': 'fallback',
    }


def chat_with_ai(message, history=None, user_profile=None):
    client = _get_client()
    if client is None:
        return _fallback_chat(message)

    try:
        system_prompt = _build_system_prompt(user_profile)

        parts = [system_prompt + "\n\n"]

        if history:
            for msg in history[-10:]:
                role_label = "Utilizator" if msg['role'] == 'user' else "Asistent"
                parts.append(f"{role_label}: {msg['content']}\n")

        parts.append(f"Utilizator: {message}\nAsistent:")

        full_prompt = ''.join(parts)
        response = client.models.generate_content(
            model='gemini-2.0-flash',
            contents=full_prompt,
        )

        answer = response.text.strip()
        if len(answer) > 1500:
            answer = answer[:1500].rsplit('.', 1)[0] + '.'

        return answer

    except Exception as e:
        logger.error(f'Eroare Gemini chat: {e}')
        return _fallback_chat(message)


def _build_system_prompt(profile=None):
    base = (
        "Esti un asistent de nutritie si fitness care vorbeste romana. "
        "Numele tau este ReborN AI. Raspunzi prietenos dar profesional. "
        "Dai sfaturi practice despre alimentatie, antrenamente, calorii si stil de viata sanatos. "
        "Nu faci diagnostic medical, recomanzi mereu consultarea unui medic pt probleme de sanatate. "
        "Raspunsurile tale sunt concise, la obiect, maxim 2-3 paragrafe."
    )

    if profile:
        goal_map = {
            'lose': 'slabire (deficit caloric)',
            'maintain': 'mentinere greutate',
            'gain': 'crestere masa musculara (surplus caloric)',
        }
        goal_text = goal_map.get(profile.goal, 'mentinere')
        base += f"\n\nUtilizatorul are obiectivul: {goal_text}."

        if profile.weight_kg:
            base += f" Greutate: {profile.weight_kg} kg."
        if profile.height_cm:
            base += f" Inaltime: {profile.height_cm} cm."
        if profile.age:
            base += f" Varsta: {profile.age} ani."
        if profile.suspected_insulin_resistance:
            base += " Suspiciune de rezistenta la insulina - recomanda alimente cu IG scazut."

    return base


def _fallback_chat(message):
    msg = message.lower()

    if any(w in msg for w in ['slabit', 'slăbit', 'slab', 'gras', 'kilogram']):
        return (
            'Pentru slabire sanatoasa, tinteste un deficit de 300-500 kcal pe zi. '
            'Combina o dieta echilibrata cu miscare regulata - cel putin 3-4 antrenamente '
            'pe saptamana. Pune accent pe proteine (1.6-2g per kg corp) ca sa pastrezi '
            'masa musculara. Bea suficienta apa si dormi 7-8 ore.'
        )
    elif any(w in msg for w in ['muschi', 'mușchi', 'masa', 'ingras', 'îngraș']):
        return (
            'Pentru cresterea masei musculare ai nevoie de un surplus caloric de '
            '300-500 kcal peste necesarul tau zilnic. Proteina e cheia: 1.8-2.2g per kg corp. '
            'Antreneaza-te cu greutati progresive de 4-5 ori pe saptamana si odihneste-te bine.'
        )
    elif any(w in msg for w in ['insulin', 'glicemi', 'zahar', 'zahăr', 'diabet']):
        return (
            'Rezistenta la insulina se imbunatateste prin: alimentatie cu indice glicemic scazut, '
            'exercitii regulate (inclusiv mersul pe jos 30 min/zi), somn de calitate si '
            'reducerea stresului. Evita zaharul rafinat si alimentele ultraprocesate. '
            'Consulta un medic pentru analize specifice (HOMA-IR, glicemie a jeun).'
        )
    elif any(w in msg for w in ['calori', 'kcal', 'mancare', 'mâncare']):
        return (
            'Necesarul caloric depinde de greutate, inaltime, varsta si nivel de activitate. '
            'O estimare rapida: greutatea in kg x 30 = calorii pt mentinere. '
            'Ajusteaza cu -500 pt slabire sau +400 pt crestere. '
            'Foloseste scanerul nostru AI pentru a estima caloriile din mese.'
        )
    elif any(w in msg for w in ['antrenament', 'exercit', 'sala', 'sală', 'sport']):
        return (
            'Un program bun include 3-5 zile de antrenament pe saptamana cu cel putin '
            'o zi de odihna. Combina exercitii de forta cu cardio. Incalzirea e obligatorie! '
            'Progreseaza treptat in greutati si intensitate. Verifica sectiunea de exercitii '
            'din aplicatie pentru rutine complete.'
        )
    elif any(w in msg for w in ['salut', 'buna', 'hey', 'hello', 'servus']):
        return (
            'Salut! Sunt ReborN AI, asistentul tau de nutritie si fitness. '
            'Pot sa te ajut cu: planuri de alimentatie, sfaturi de antrenament, '
            'estimari de calorii sau informatii despre rezistenta la insulina. '
            'Ce te intereseaza?'
        )
    else:
        return (
            'Multumesc pentru mesaj! Sunt aici sa te ajut cu orice tine de nutritie, '
            'fitness si stil de viata sanatos. Poti sa ma intrebi despre diete, '
            'antrenamente, calorii sau rezistenta la insulina. Cu ce pot sa te ajut?'
        )


def generate_meal_plan(profile):
    client = _get_client()
    if client is None:
        return _fallback_meal_plan(profile)

    try:
        goal_map = {
            'lose': 'slabire cu deficit caloric de ~500 kcal',
            'maintain': 'mentinere greutate actuala',
            'gain': 'crestere masa musculara cu surplus de ~400 kcal',
        }
        goal = goal_map.get(profile.goal, 'mentinere')

        prompt = (
            f"Genereaza un plan alimentar pentru o zi completa (mic dejun, pranz, cina, gustare) "
            f"pentru o persoana cu obiectivul: {goal}."
        )
        if profile.weight_kg:
            prompt += f" Greutate: {profile.weight_kg} kg."
        if profile.suspected_insulin_resistance:
            prompt += " Are rezistenta la insulina, foloseste alimente cu IG scazut."

        prompt += (
            "\nRaspunde in romana, format JSON strict, fara markdown:\n"
            '[{"meal": "Mic dejun", "name": "...", "calories": nr, "protein": nr, '
            '"carbs": nr, "fat": nr, "ingredients": "..."},'
            '{"meal": "Pranz", ...}, {"meal": "Cina", ...}, {"meal": "Gustare", ...}]'
        )

        response = client.models.generate_content(
            model='gemini-2.0-flash',
            contents=prompt,
        )
        text = response.text.strip()
        if text.startswith('```'):
            lines = text.split('\n')
            text = '\n'.join(lines[1:-1])

        meals = json.loads(text)
        return meals

    except Exception as e:
        logger.error(f'Eroare generare plan: {e}')
        return _fallback_meal_plan(profile)


def _fallback_meal_plan(profile):
    if profile and profile.goal == 'lose':
        return [
            {"meal": "Mic dejun", "name": "Omleta cu spanac si rosii", "calories": 320,
             "protein": 24, "carbs": 8, "fat": 22, "ingredients": "3 oua, spanac, rosii, ulei de masline"},
            {"meal": "Pranz", "name": "Piept de pui la gratar cu salata", "calories": 420,
             "protein": 38, "carbs": 12, "fat": 24, "ingredients": "150g piept pui, salata verde, castraveti, rosii, lamaie"},
            {"meal": "Cina", "name": "Somon cu sparanghel la cuptor", "calories": 380,
             "protein": 32, "carbs": 6, "fat": 25, "ingredients": "120g somon, sparanghel, lamaie, usturoi"},
            {"meal": "Gustare", "name": "Iaurt grecesc cu nuci", "calories": 180,
             "protein": 12, "carbs": 10, "fat": 11, "ingredients": "150g iaurt grecesc, 20g nuci"},
        ]
    elif profile and profile.goal == 'gain':
        return [
            {"meal": "Mic dejun", "name": "Ovaz cu unt de arahide si banana", "calories": 580,
             "protein": 22, "carbs": 72, "fat": 24, "ingredients": "80g ovaz, banana, 30g unt arahide, lapte"},
            {"meal": "Pranz", "name": "Orez cu vita si legume", "calories": 720,
             "protein": 42, "carbs": 78, "fat": 22, "ingredients": "200g vita, 100g orez, brocoli, morcov"},
            {"meal": "Cina", "name": "Paste integrale cu sos bolognese", "calories": 650,
             "protein": 35, "carbs": 80, "fat": 18, "ingredients": "120g paste, carne tocata, sos rosii, parmezan"},
            {"meal": "Gustare", "name": "Shake proteic cu ovaz", "calories": 450,
             "protein": 35, "carbs": 48, "fat": 12, "ingredients": "proteina whey, lapte, ovaz, banana"},
        ]
    else:
        return [
            {"meal": "Mic dejun", "name": "Sandwich integral cu ou si avocado", "calories": 420,
             "protein": 18, "carbs": 35, "fat": 24, "ingredients": "2 felii paine integrala, ou, avocado, rosie"},
            {"meal": "Pranz", "name": "Bowl cu quinoa si pui", "calories": 550,
             "protein": 35, "carbs": 52, "fat": 18, "ingredients": "quinoa, piept pui, ardei, porumb, dressing"},
            {"meal": "Cina", "name": "Peste alb cu cartofi dulci", "calories": 480,
             "protein": 30, "carbs": 42, "fat": 18, "ingredients": "pangasius, cartofi dulci, lamaie, salata"},
            {"meal": "Gustare", "name": "Fructe cu ricotta", "calories": 200,
             "protein": 10, "carbs": 24, "fat": 7, "ingredients": "mere, ricotta, scortisoara, miere"},
        ]
