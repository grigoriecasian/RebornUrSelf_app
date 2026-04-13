# RebornUrSelf

Platforma web de nutritie, fitness si wellness construita cu Django.

## Functionalitati

- **Tracker calorii** - inregistrare zilnica a alimentelor cu macro-nutrienti (proteine, carbohidrati, grasimi)
- **Diete personalizate** - 10 planuri alimentare cu retete pentru fiecare zi a saptamanii
- **Antrenamente** - exercitii pentru acasa, sala si aer liber, filtrate dupa dificultate
- **Scanner AI** - analiza fotografiilor cu mancare folosind Google Gemini Vision
- **AI Chat (VIP)** - asistent personal de nutritie si fitness
- **Check-in zilnic** - monitorizare obiceiuri (dieta, sport, apa, somn)
- **Progres** - grafice evolutie greutate, calorii si scor check-in pe 14 zile
- **Achievements** - 10 realizari deblocabile pe baza activitatii
- **Notificari** - remindere automate pentru check-in si logare alimente
- **Export** - descarcare progres in format CSV sau varianta printabila PDF
- **Dark / Light mode** - tema salvata in localStorage
- **Chestionar insulina** - evaluare risc rezistenta la insulina

## Tehnologii

- Python 3.13 / Django 5.2
- Tailwind CSS (CDN)
- JavaScript vanilla (grafice Canvas, interactivitate)
- Google Gemini API (analiza imagini, chat AI, generare planuri)
- SQLite

## Instalare

```bash
git clone https://github.com/grigoriecasian/RebornUrSelf_app.git
cd RebornUrSelf_app/RebornUrSelf
pip install -r requirements.txt
```

Creeaza un fisier `.env` (optional, pentru AI):
```
GEMINI_API_KEY=cheia_ta_de_la_ai.google.dev
```

Initializeaza baza de date:
```bash
python manage.py migrate
python manage.py seed_data
python manage.py setup_achievements
```

Porneste serverul:
```bash
python manage.py runserver
```

Acceseaza aplicatia la `http://127.0.0.1:8000`

## Structura proiect

```
RebornUrSelf/
    manage.py
    RebornUrSelf/          # configurare Django (settings, urls)
    my_app/
        models.py          # UserProfile, Diet, Recipe, Workout, DailyLog, etc.
        views.py           # logica aplicatiei
        forms.py           # formulare
        ai_utils.py        # integrare Google Gemini API
        urls.py            # rutele aplicatiei
        templates/wellness/ # 22 template-uri HTML
        static/wellness/   # CSS
```

## Autor

Grafos
