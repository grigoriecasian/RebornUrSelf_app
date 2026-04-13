from django.core.management.base import BaseCommand
from my_app.models import (
    Diet, Recipe, Workout,
    Citat, Reteta, Exercitiu, ProgramZilnic,
)


class Command(BaseCommand):
    help = 'Populeaza baza de date cu date initiale (diete, retete, antrenamente, citate).'

    def handle(self, *args, **options):
        self._seed_diets()
        self._seed_workouts()
        self._seed_citate()
        self._seed_retete_index()
        self._seed_exercitii_index()
        self._seed_program_zilnic()
        self.stdout.write(self.style.SUCCESS('\nBaza de date a fost populata.'))

    def _seed_diets(self):
        self.stdout.write('--- Diete si retete ---')

        # === DIETA 1: Deficit caloric echilibrat (slabire) ===
        d1, _ = Diet.objects.get_or_create(
            name='Deficit Caloric Echilibrat',
            defaults={
                'goal': 'lose',
                'description': 'Plan alimentar cu deficit moderat de 500 kcal, bazat pe proteine slabe, '
                               'legume si grasimi sanatoase. Ideal pentru pierderea in greutate sustinuta.',
                'calories_per_day': 1500,
                'is_insulin_friendly': True,
            }
        )
        d1_recipes = [
            # Luni
            {'title': 'Omleta cu spanac si rosii', 'description': 'Mic dejun bogat in proteine cu legume proaspete.',
             'ingredients': '3 oua, 50g spanac, 1 rosie, sare, piper', 'instructions': 'Bate ouale, adauga spanacul si rosiile taiate. Gateste la foc mediu 3-4 minute pe fiecare parte.', 'calories': 320, 'day': 1, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=400&h=300&fit=crop'},

            {'title': 'Piept de pui la gratar cu salata', 'description': 'Pranz usor dar satios cu proteine de calitate.',
             'ingredients': '150g piept pui, salata verde, castravete, rosii, ulei masline, lamaie',
             'instructions': 'Grieleaza puiul 6-7 min pe parte. Amesteca legumele, adauga ulei si lamaie.', 'calories': 420, 'day': 1, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=400&h=300&fit=crop'},

            {'title': 'Supa crema de brocoli', 'description': 'Cina usoara, bogata in fibre si vitamine.',
             'ingredients': '300g brocoli, 1 cartof mic, ceapa, usturoi, 100ml lapte',
             'instructions': 'Fierbe legumele 15 min. Mixeaza cu laptele si condimenteaza.', 'calories': 220, 'day': 1, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1476718406336-bb5a9690ee2a?w=400&h=300&fit=crop'},

            {'title': 'Mar cu unt de migdale', 'description': 'Gustare simpla cu grasimi sanatoase.',
             'ingredients': '1 mar verde, 15g unt de migdale',
             'instructions': 'Taie marul felii si unge cu unt de migdale.', 'calories': 160, 'day': 1, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1490474418585-ba9bad8fd0ea?w=400&h=300&fit=crop'},


            # Marti
            {'title': 'Iaurt grecesc cu afine si nuci', 'description': 'Mic dejun rapid, bogat in proteine si antioxidanti.',
             'ingredients': '200g iaurt grecesc 2%, 80g afine, 15g nuci, scortisoara',
             'instructions': 'Pune iaurtul in bol, adauga afinele, nucile si scortisoara.', 'calories': 280, 'day': 2, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1488477181946-6428a0291777?w=400&h=300&fit=crop'},

            {'title': 'Salata cu ton si fasole', 'description': 'Pranz satios cu proteine complete si fibre.',
             'ingredients': '100g ton in apa, 100g fasole alba, rosii, ceapa rosie, patrunjel, ulei masline',
             'instructions': 'Scurge tonul si fasolea. Amesteca cu legumele taiate marunt. Adauga ulei si lamaie.', 'calories': 380, 'day': 2, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=400&h=300&fit=crop'},

            {'title': 'Somon la cuptor cu sparanghel', 'description': 'Cina bogata in omega-3 si fibre.',
             'ingredients': '120g somon, sparanghel, usturoi, lamaie, ulei masline',
             'instructions': 'Aseaza somonul si sparanghelul pe tava. Condimenteaza si coace 18 min la 200°C.', 'calories': 380, 'day': 2, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1467003909585-2f8a72700288?w=400&h=300&fit=crop'},

            {'title': 'Morcovi cu hummus', 'description': 'Gustare crocanta si sanatoasa.',
             'ingredients': '2 morcovi, 40g hummus',
             'instructions': 'Taie morcovii batoane si serveste cu hummus.', 'calories': 130, 'day': 2, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1585937421612-70a008356fbe?w=400&h=300&fit=crop'},


            # Miercuri
            {'title': 'Smoothie verde proteic', 'description': 'Mic dejun lichid energizant si nutritiv.',
             'ingredients': '200ml lapte migdale, 1 banana, 50g spanac, 25g whey vanilie, gheata',
             'instructions': 'Pune totul in blender si mixeaza 40 secunde.', 'calories': 290, 'day': 3, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1505252585461-04db1eb84625?w=400&h=300&fit=crop'},

            {'title': 'Bowl cu quinoa, pui si avocado', 'description': 'Pranz complet cu toate grupele de macros.',
             'ingredients': '80g quinoa, 120g piept pui, 1/2 avocado, rosii cherry, porumb',
             'instructions': 'Fierbe quinoa 15 min. Grieleaza puiul, taie avocado. Asambleaza bolul.', 'calories': 450, 'day': 3, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400&h=300&fit=crop'},

            {'title': 'Peste alb cu legume la aburi', 'description': 'Cina usoara, digerarea rapida.',
             'ingredients': '150g pangasius, brocoli, morcov, fasole verde, lamaie',
             'instructions': 'Gateste pestele si legumele la aburi 12 min. Adauga lamaie.', 'calories': 280, 'day': 3, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1467003909585-2f8a72700288?w=400&h=300&fit=crop'},

            {'title': 'Iaurt cu seminte de chia', 'description': 'Gustare bogata in omega-3 si fibre.',
             'ingredients': '100g iaurt, 10g seminte chia, cateva zmeura',
             'instructions': 'Amesteca iaurtul cu semintele. Lasa 10 min si adauga fructele.', 'calories': 140, 'day': 3, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1488477181946-6428a0291777?w=400&h=300&fit=crop'},


            # Joi
            {'title': 'Oua posat pe paine integrala', 'description': 'Mic dejun clasic cu proteine si fibre.',
             'ingredients': '2 oua, 1 felie paine integrala, avocado, ardei iute (optional)',
             'instructions': 'Posaza ouale 3-4 min in apa clocotita cu otet. Pune pe paine cu avocado.', 'calories': 310, 'day': 4, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=400&h=300&fit=crop'},

            {'title': 'Wrap cu curcan si legume', 'description': 'Pranz usor si rapid de preparat.',
             'ingredients': '1 tortilla integrala, 100g piept curcan, salata, rosii, mustar',
             'instructions': 'Pune curcanul si legumele pe tortilla. Adauga mustar si ruleaza.', 'calories': 370, 'day': 4, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400&h=300&fit=crop'},

            {'title': 'Tocana de linte cu legume', 'description': 'Cina vegetariana bogata in fibre si proteine.',
             'ingredients': '100g linte rosie, rosii, morcov, ceapa, usturoi, boia, cimbru',
             'instructions': 'Caleste ceapa si morcovul. Adauga lintea, rosiile si 400ml apa. Fierbe 20 min.', 'calories': 340, 'day': 4, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1585937421612-70a008356fbe?w=400&h=300&fit=crop'},

            {'title': 'Castravete cu branza cottage', 'description': 'Gustare usoara si racoritoare.',
             'ingredients': '1 castravete, 80g branza cottage, marar',
             'instructions': 'Taie castravetele rondele, adauga branza si mararul.', 'calories': 100, 'day': 4, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1452195100486-9cc805987862?w=400&h=300&fit=crop'},


            # Vineri
            {'title': 'Clatite proteice cu afine', 'description': 'Mic dejun dulce dar sanatos.',
             'ingredients': '1 banana, 2 oua, 30g fulgi ovaz, afine, scortisoara',
             'instructions': 'Mixeaza banana, ouale si ovazul. Prajeste pe ambele parti. Adauga afinele.', 'calories': 320, 'day': 5, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1567620905732-2d1ec7ab7445?w=400&h=300&fit=crop'},

            {'title': 'Salata greceasca cu pui', 'description': 'Pranz mediteranean cu proteine.',
             'ingredients': '120g pui grilat, rosii, castravete, ardei, ceapa, masline, feta, ulei masline',
             'instructions': 'Grieleaza puiul. Taie legumele. Amesteca totul cu ulei si oregano.', 'calories': 430, 'day': 5, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=400&h=300&fit=crop'},

            {'title': 'Omleta cu ciuperci si ardei', 'description': 'Cina rapida si satioasa.',
             'ingredients': '3 oua, 100g ciuperci, 1 ardei, ceapa verde, cascaval light',
             'instructions': 'Caleste ciupercile si ardeiul. Adauga ouale batute. Presara cascaval.', 'calories': 300, 'day': 5, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=400&h=300&fit=crop'},

            {'title': 'Smoothie cu capsuni', 'description': 'Gustare racoritoare si usoara.',
             'ingredients': '150g capsuni, 100ml lapte, 5 cuburi gheata',
             'instructions': 'Mixeaza totul 30 secunde.', 'calories': 90, 'day': 5, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1505252585461-04db1eb84625?w=400&h=300&fit=crop'},


            # Sambata
            {'title': 'Avocado toast cu ou', 'description': 'Mic dejun popular si nutritiv.',
             'ingredients': '1 felie paine integrala, 1/2 avocado, 1 ou fiert, fulgi chili, lamaie',
             'instructions': 'Prajeste painea. Zdrobeste avocado cu lamaie, intinde pe paine. Pune oul taiat.', 'calories': 330, 'day': 6, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=400&h=300&fit=crop'},

            {'title': 'Supa de pui cu legume', 'description': 'Pranz cald si reconfortant.',
             'ingredients': '120g piept pui, morcov, telina, pastarnac, ceapa, patrunjel',
             'instructions': 'Fierbe puiul cu legumele 30 min. Toaca verdeatza si adaug-o la sfarsit.', 'calories': 350, 'day': 6, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400&h=300&fit=crop'},

            {'title': 'Dovlecei umpluti cu carne tocata', 'description': 'Cina cu putini carbohidrati.',
             'ingredients': '2 dovlecei, 150g carne tocata pui, rosii, ceapa, usturoi, parmezan',
             'instructions': 'Scobeaza dovleceii. Caleste carnea cu ceapa si rosiile. Umple si coace 25 min.', 'calories': 340, 'day': 6, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1540420773420-3366772f4999?w=400&h=300&fit=crop'},

            {'title': 'Migdale crude si mar', 'description': 'Gustare cu grasimi bune si fibre.',
             'ingredients': '15g migdale crude, 1 mar mic',
             'instructions': 'Serveste asa cum sunt.', 'calories': 150, 'day': 6, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1473093295043-cdd812d0e601?w=400&h=300&fit=crop'},


            # Duminica
            {'title': 'Granola cu iaurt si fructe', 'description': 'Mic dejun festiv dar echilibrat.',
             'ingredients': '30g granola fara zahar, 150g iaurt grecesc, kiwi, capsuni',
             'instructions': 'Pune iaurtul, granola deasupra si decoreaza cu fructe.', 'calories': 290, 'day': 7, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1488477181946-6428a0291777?w=400&h=300&fit=crop'},

            {'title': 'Pulpe de pui cu salata de varza', 'description': 'Pranz traditional adaptat dietei.',
             'ingredients': '150g pulpa pui dezosata, varza, morcov, otet, ulei masline',
             'instructions': 'Grieleaza pulpa de pui. Rade varza si morcovul, adauga otet si ulei.', 'calories': 400, 'day': 7, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=400&h=300&fit=crop'},

            {'title': 'Ciorba de legume', 'description': 'Cina usoara traditionala.',
             'ingredients': 'morcov, cartofi, fasole verde, rosii, ceapa, patrunjel, bors',
             'instructions': 'Fierbe legumele 25 min. Adauga borsul si verdeatza la final.', 'calories': 200, 'day': 7, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1476718406336-bb5a9690ee2a?w=400&h=300&fit=crop'},

            {'title': 'Pere cu scortisoara', 'description': 'Gustare dulce naturala.',
             'ingredients': '1 para, scortisoara, 5g miere',
             'instructions': 'Taie para felii, presara scortisoara si adauga un strop de miere.', 'calories': 100, 'day': 7, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1490474418585-ba9bad8fd0ea?w=400&h=300&fit=crop'},

        ]
        for r in d1_recipes:
            Recipe.objects.get_or_create(diet=d1, title=r['title'], day=r['day'], defaults=r)

        # === DIETA 2: Echilibru nutritional (mentinere) ===
        d2, _ = Diet.objects.get_or_create(
            name='Echilibru Nutritional',
            defaults={
                'goal': 'maintain',
                'description': 'Plan alimentar echilibrat cu toate grupele de macronutrienti. '
                               'Pentru mentinerea greutatii si un stil de viata activ.',
                'calories_per_day': 2200,
                'is_insulin_friendly': False,
            }
        )
        d2_recipes = [
            # Luni
            {'title': 'Sandwich integral cu ou si avocado', 'description': 'Mic dejun complet si energizant.',
             'ingredients': '2 felii paine integrala, 2 oua, 1/2 avocado, rosie',
             'instructions': 'Prajeste ouale, taie avocado felii. Asambleaza sandwichul.', 'calories': 450, 'day': 1, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=400&h=300&fit=crop'},

            {'title': 'Paste cu sos bolognese', 'description': 'Pranz clasic, consistent si gustos.',
             'ingredients': '100g paste, 150g carne tocata vita, sos rosii, ceapa, usturoi, busuioc',
             'instructions': 'Caleste ceapa si usturoiul, adauga carnea, apoi sosul. Fierbe pastele separat si combina.', 'calories': 620, 'day': 1, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1551183053-bf91a1d81141?w=400&h=300&fit=crop'},

            {'title': 'Bowl cu quinoa si legume', 'description': 'Cina usoara dar completa nutritional.',
             'ingredients': '80g quinoa, ardei, porumb, fasole, avocado, lime',
             'instructions': 'Fierbe quinoa. Taie legumele si amesteca totul. Adauga lime.', 'calories': 480, 'day': 1, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1512058564366-18510be2db19?w=400&h=300&fit=crop'},

            {'title': 'Trail mix cu fructe uscate', 'description': 'Gustare energizanta pentru dupa-amiaza.',
             'ingredients': '20g migdale, 15g stafide, 10g seminte dovleac',
             'instructions': 'Amesteca si serveste.', 'calories': 190, 'day': 1, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1490474418585-ba9bad8fd0ea?w=400&h=300&fit=crop'},


            # Marti
            {'title': 'Clatite cu ovaz si banane', 'description': 'Mic dejun dulce si energizant.',
             'ingredients': '50g fulgi ovaz, 1 banana, 2 oua, scortisoara, miere',
             'instructions': 'Mixeaza banana cu ouale si ovazul. Prajeste pe ambele parti 2-3 min.', 'calories': 420, 'day': 2, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1567620905732-2d1ec7ab7445?w=400&h=300&fit=crop'},

            {'title': 'Friptura de curcan cu piure', 'description': 'Pranz consistent cu proteine si carbohidrati.',
             'ingredients': '150g piept curcan, 200g cartofi, 50ml lapte, unt, salata verde',
             'instructions': 'Grieleaza curcanul. Fierbe cartofii si fa piure cu lapte si unt.', 'calories': 580, 'day': 2, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400&h=300&fit=crop'},

            {'title': 'Tacos cu peste si salsa', 'description': 'Cina mexicana usoara si gustoasa.',
             'ingredients': '120g cod, 2 tortillas mici, varza, rosii, avocado, lamaie, coriandru',
             'instructions': 'Prajeste pestele. Toaca legumele pt salsa. Asambleaza tacos.', 'calories': 480, 'day': 2, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1467003909585-2f8a72700288?w=400&h=300&fit=crop'},

            {'title': 'Banana cu unt de arahide', 'description': 'Gustare rapida cu energie sustinuta.',
             'ingredients': '1 banana, 15g unt de arahide',
             'instructions': 'Taie banana si adauga untul de arahide deasupra.', 'calories': 210, 'day': 2, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1490474418585-ba9bad8fd0ea?w=400&h=300&fit=crop'},


            # Miercuri
            {'title': 'Porridge cu mere si scortisoara', 'description': 'Mic dejun cald si reconfortant.',
             'ingredients': '60g fulgi ovaz, 250ml lapte, 1 mar, scortisoara, nuci',
             'instructions': 'Fierbe ovazul in lapte 5 min. Adauga marul ras, scortisoara si nucile.', 'calories': 400, 'day': 3, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1517673400267-0251440c45dc?w=400&h=300&fit=crop'},

            {'title': 'Burger de vita cu cartofi dulci', 'description': 'Pranz gustos si echilibrat.',
             'ingredients': '150g vita tocata, 1 chifluta integrala, salata, rosie, 150g cartofi dulci',
             'instructions': 'Formeaza burgerul si grieleaza 5 min/parte. Coace cartofii dulci felii 20 min.', 'calories': 650, 'day': 3, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1558030006-450675393462?w=400&h=300&fit=crop'},

            {'title': 'Risotto cu ciuperci', 'description': 'Cina cremoasa si aromata.',
             'ingredients': '80g orez arborio, 150g ciuperci, ceapa, usturoi, parmezan, vin alb',
             'instructions': 'Caleste ceapa, adauga orezul. Adauga vin, apoi supa treptat. Incorporeaza ciupercile.', 'calories': 480, 'day': 3, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1476124369491-e7addf5db371?w=400&h=300&fit=crop'},

            {'title': 'Iaurt cu granola', 'description': 'Gustare crocanta si proteica.',
             'ingredients': '150g iaurt, 25g granola, miere',
             'instructions': 'Pune iaurtul in bol cu granola si un fir de miere.', 'calories': 200, 'day': 3, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1488477181946-6428a0291777?w=400&h=300&fit=crop'},


            # Joi
            {'title': 'Omleta frantuzeasca cu verdeata', 'description': 'Mic dejun elegant si usor de facut.',
             'ingredients': '3 oua, unt, ceapa verde, marar, branza de capra',
             'instructions': 'Bate ouale usor. Gateste in unt pe o parte, adauga umplutura si impatureste.', 'calories': 380, 'day': 4, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=400&h=300&fit=crop'},

            {'title': 'Pui teriyaki cu orez', 'description': 'Pranz inspirat din bucataria asiatica.',
             'ingredients': '150g piept pui, 100g orez, sos soia, miere, usturoi, ghimbir, susan',
             'instructions': 'Fa sosul teriyaki. Prajeste puiul in sos. Serveste pe orez.', 'calories': 600, 'day': 4, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400&h=300&fit=crop'},

            {'title': 'Salata Caesar cu crutoane', 'description': 'Cina clasica, usoara si gustoasa.',
             'ingredients': 'salata romana, pui grilat, crutoane, parmezan, dressing Caesar',
             'instructions': 'Grieleaza puiul, taie-l felii. Amesteca cu salata, crutoane si dressing.', 'calories': 480, 'day': 4, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=400&h=300&fit=crop'},

            {'title': 'Biscuiti de ovaz cu banana', 'description': 'Gustare sanatoasa facuta acasa.',
             'ingredients': '1 banana, 40g fulgi ovaz, scortisoara',
             'instructions': 'Zdrobeste banana, amesteca cu ovazul. Formeaza biscuiti. Coace 15 min la 180°C.', 'calories': 170, 'day': 4, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1490474418585-ba9bad8fd0ea?w=400&h=300&fit=crop'},


            # Vineri
            {'title': 'Muesli cu lapte si fructe', 'description': 'Mic dejun rapid si energizant.',
             'ingredients': '50g muesli, 200ml lapte, 1 banana, cateva capsuni',
             'instructions': 'Toarna laptele peste muesli, adauga fructele taiate.', 'calories': 380, 'day': 5, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1488477181946-6428a0291777?w=400&h=300&fit=crop'},

            {'title': 'Somon cu paste si sos pesto', 'description': 'Pranz gourmet rapid.',
             'ingredients': '120g somon, 80g paste, pesto, rosii uscate, rucola',
             'instructions': 'Prajeste somonul. Fierbe pastele, amesteca cu pesto. Adauga somonul deasupra.', 'calories': 620, 'day': 5, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1467003909585-2f8a72700288?w=400&h=300&fit=crop'},

            {'title': 'Pizza integrala cu legume', 'description': 'Cina de vineri sanatoasa.',
             'ingredients': 'blat integral, sos rosii, mozzarella, ardei, ciuperci, masline, rucola',
             'instructions': 'Intinde sosul pe blat, adauga toppinguri. Coace 12 min la 220°C.', 'calories': 520, 'day': 5, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=400&h=300&fit=crop'},

            {'title': 'Fructe proaspete asortate', 'description': 'Gustare naturala si racoritoare.',
             'ingredients': 'portocala, kiwi, cateva struguri',
             'instructions': 'Taie fructele si serveste.', 'calories': 150, 'day': 5, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1490474418585-ba9bad8fd0ea?w=400&h=300&fit=crop'},


            # Sambata
            {'title': 'French toast cu fructe', 'description': 'Mic dejun festiv de weekend.',
             'ingredients': '2 felii paine, 2 oua, 50ml lapte, scortisoara, capsuni, sirop artar',
             'instructions': 'Inmoaie painea in amestecul de oua si lapte. Prajeste pana e aurie.', 'calories': 450, 'day': 6, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1484723091739-30a097e8f929?w=400&h=300&fit=crop'},

            {'title': 'Gyros cu lipie si tzatziki', 'description': 'Pranz grecesc gustos.',
             'ingredients': '150g pui condimentat, lipie, rosii, ceapa, tzatziki, salata',
             'instructions': 'Grieleaza puiul feliat. Asambleaza in lipie cu legume si tzatziki.', 'calories': 580, 'day': 6, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1626700051175-6818013e1d4f?w=400&h=300&fit=crop'},

            {'title': 'Paste carbonara', 'description': 'Cina clasica italiana.',
             'ingredients': '100g spaghetti, 80g pancetta, 2 galbenusuri, parmezan, piper',
             'instructions': 'Fierbe pastele. Prajeste pancetta. Amesteca galbenusurile cu parmezanul. Combina totul.', 'calories': 560, 'day': 6, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1551183053-bf91a1d81141?w=400&h=300&fit=crop'},

            {'title': 'Popcorn simplu', 'description': 'Gustare usoara de seara.',
             'ingredients': '30g porumb de popcorn, putina sare',
             'instructions': 'Prepara popcornul in cratita cu capac. Adauga sare.', 'calories': 120, 'day': 6, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1473093295043-cdd812d0e601?w=400&h=300&fit=crop'},


            # Duminica
            {'title': 'Briosa cu oua si legume', 'description': 'Mic dejun pregatit la cuptor.',
             'ingredients': '4 oua, spanac, ardei rosu, branza feta, ceapa verde',
             'instructions': 'Bate ouale, adauga legumele. Pune in forme de briosa. Coace 20 min la 180°C.', 'calories': 350, 'day': 7, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=400&h=300&fit=crop'},

            {'title': 'Tocana de vita cu cartofi', 'description': 'Pranz traditional de duminica.',
             'ingredients': '180g vita, cartofi, morcov, ceapa, rosii, boia, cimbru',
             'instructions': 'Caleste carnea si ceapa. Adauga legumele si apa. Gateste la foc mic 45 min.', 'calories': 620, 'day': 7, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1558030006-450675393462?w=400&h=300&fit=crop'},

            {'title': 'Suprem de pui cu legume la gratar', 'description': 'Cina usoara si gustoasa.',
             'ingredients': '150g piept pui, dovlecel, vinete, ardei, ulei masline, ierburi',
             'instructions': 'Grieleaza puiul si legumele. Condimenteaza cu ierburi si ulei.', 'calories': 400, 'day': 7, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400&h=300&fit=crop'},

            {'title': 'Ciocolata neagra si migdale', 'description': 'Gustare cu antioxidanti.',
             'ingredients': '20g ciocolata neagra 70%, 10g migdale',
             'instructions': 'Savureaza lent.', 'calories': 150, 'day': 7, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1473093295043-cdd812d0e601?w=400&h=300&fit=crop'},

        ]
        for r in d2_recipes:
            Recipe.objects.get_or_create(diet=d2, title=r['title'], day=r['day'], defaults=r)

        # === DIETA 3: Surplus masa musculara ===
        d3, _ = Diet.objects.get_or_create(
            name='Surplus pentru Masa Musculara',
            defaults={
                'goal': 'gain',
                'description': 'Plan hipercaloric cu accent pe proteine si carbohidrati complecsi. '
                               'Conceput pentru cresterea masei musculare curate.',
                'calories_per_day': 3000,
                'is_insulin_friendly': False,
            }
        )
        d3_recipes = [
            # Luni
            {'title': 'Porridge cu unt de arahide si banana', 'description': 'Mic dejun caloric si bogat in energie.',
             'ingredients': '80g fulgi ovaz, 30g unt arahide, banana, 250ml lapte, miere',
             'instructions': 'Fierbe ovazul in lapte 5 min. Adauga untul de arahide, banana taiata si miere.', 'calories': 620, 'day': 1, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1490474418585-ba9bad8fd0ea?w=400&h=300&fit=crop'},

            {'title': 'Orez cu vita si brocoli', 'description': 'Masa principala pentru dezvoltare musculara.',
             'ingredients': '200g vita, 120g orez, brocoli, sos soia, ulei susan',
             'instructions': 'Gateste orezul. Prajeste vita la foc mare 3 min, adauga brocoli si sosul.', 'calories': 750, 'day': 1, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1558030006-450675393462?w=400&h=300&fit=crop'},

            {'title': 'Paste integrale cu piept de pui', 'description': 'Cina consistenta bogata in proteine.',
             'ingredients': '120g paste integrale, 180g piept pui, sos rosii, parmezan',
             'instructions': 'Fierbe pastele. Grieleaza puiul, taie-l si amesteca cu pastele si sosul.', 'calories': 680, 'day': 1, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400&h=300&fit=crop'},

            {'title': 'Shake de masa cu ovaz', 'description': 'Gustare hipercalorica intre mese.',
             'ingredients': '40g whey, 300ml lapte, banana, 40g fulgi ovaz, 15g unt arahide',
             'instructions': 'Pune totul in blender si mixeaza 40 secunde.', 'calories': 520, 'day': 1, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1505252585461-04db1eb84625?w=400&h=300&fit=crop'},


            # Marti
            {'title': 'Oua scrambled cu paine si branza', 'description': 'Mic dejun clasic hipercaloric.',
             'ingredients': '4 oua, 2 felii paine alba, 30g cascaval, unt, rosie',
             'instructions': 'Scramble ouale in unt. Serveste pe paine cu cascaval si rosie.', 'calories': 580, 'day': 2, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=400&h=300&fit=crop'},

            {'title': 'Pui tikka masala cu orez basmati', 'description': 'Pranz aromat cu proteine si carbohidrati.',
             'ingredients': '200g piept pui, 150g orez basmati, iaurt, pasta curry, rosii, smantana',
             'instructions': 'Marineaza puiul in iaurt si curry. Prajeste, adauga sosul. Serveste cu orez.', 'calories': 780, 'day': 2, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400&h=300&fit=crop'},

            {'title': 'Burger dublu cu cartofi', 'description': 'Cina substantiala pentru crestere.',
             'ingredients': '250g vita tocata, 1 chifluta mare, salata, rosie, cascaval, 150g cartofi la cuptor',
             'instructions': 'Formeaza 2 chiftele, grieleaza. Asambleaza burgerul. Coace cartofii.', 'calories': 850, 'day': 2, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=400&h=300&fit=crop'},

            {'title': 'Batoane proteice cu ovaz', 'description': 'Gustare densa caloric.',
             'ingredients': '50g ovaz, 30g whey, 20g unt arahide, 15g miere, ciocolata neagra',
             'instructions': 'Amesteca totul, preseaza intr-o forma. Refrigereaza 1 ora.', 'calories': 380, 'day': 2, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1517673400267-0251440c45dc?w=400&h=300&fit=crop'},


            # Miercuri
            {'title': 'Smoothie caloric cu ovaz', 'description': 'Mic dejun lichid hipercaloric.',
             'ingredients': '300ml lapte, 40g whey, banana, 40g ovaz, 20g unt arahide, miere',
             'instructions': 'Mixeaza totul in blender 45 secunde.', 'calories': 650, 'day': 3, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1505252585461-04db1eb84625?w=400&h=300&fit=crop'},

            {'title': 'Spaghete cu chiftelute de vita', 'description': 'Pranz italian bogat in calorii.',
             'ingredients': '120g spaghetti, 200g vita tocata, sos rosii, ceapa, usturoi, parmezan',
             'instructions': 'Formeaza chiftelutele. Prajeste-le, apoi gateste-le in sos 15 min. Fierbe pastele.', 'calories': 780, 'day': 3, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1558030006-450675393462?w=400&h=300&fit=crop'},

            {'title': 'Somon cu cartofi dulci si broccoli', 'description': 'Cina bogata in omega-3 si carbohidrati.',
             'ingredients': '150g somon, 200g cartofi dulci, brocoli, ulei masline',
             'instructions': 'Coace somonul si cartofii dulci 20 min la 200°C. Gateste brocoli la aburi.', 'calories': 650, 'day': 3, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1467003909585-2f8a72700288?w=400&h=300&fit=crop'},

            {'title': 'Sandwich cu unt de arahide si banana', 'description': 'Gustare calorie-dense.',
             'ingredients': '2 felii paine, 30g unt arahide, 1 banana',
             'instructions': 'Intinde untul de arahide pe paine. Adauga banana taiata.', 'calories': 450, 'day': 3, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1528735602780-2552fd46c7af?w=400&h=300&fit=crop'},


            # Joi
            {'title': 'Omleta mare cu cascaval si sunca', 'description': 'Mic dejun proteic consistent.',
             'ingredients': '4 oua, 50g sunca, 40g cascaval, ardei, paine',
             'instructions': 'Bate ouale, adauga sunca si ardeiul. Gateste si adauga cascaval la final.', 'calories': 600, 'day': 4, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=400&h=300&fit=crop'},

            {'title': 'Steak de vita cu orez si fasole', 'description': 'Pranz pentru masa musculara.',
             'ingredients': '200g steak vita, 120g orez, fasole verde, unt, usturoi',
             'instructions': 'Gateste steakul la temperatura dorita. Fierbe orezul si fasolea separat.', 'calories': 800, 'day': 4, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1558030006-450675393462?w=400&h=300&fit=crop'},

            {'title': 'Wrap-uri mari cu pui si guacamole', 'description': 'Cina rapida si calorica.',
             'ingredients': '2 tortillas mari, 180g pui, avocado, rosii, smantana, porumb',
             'instructions': 'Grieleaza puiul. Fa guacamole. Asambleaza wrap-urile.', 'calories': 720, 'day': 4, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400&h=300&fit=crop'},

            {'title': 'Iaurt cu granola si miere', 'description': 'Gustare proteica si energizanta.',
             'ingredients': '200g iaurt grecesc, 40g granola, 15g miere, nuci',
             'instructions': 'Combina totul in bol.', 'calories': 380, 'day': 4, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1488477181946-6428a0291777?w=400&h=300&fit=crop'},


            # Vineri
            {'title': 'French toast cu sirop si fructe', 'description': 'Mic dejun bogat in carbohidrati.',
             'ingredients': '3 felii paine, 3 oua, lapte, scortisoara, capsuni, sirop artar',
             'instructions': 'Inmoaie painea, prajeste pe ambele parti. Serveste cu fructe si sirop.', 'calories': 580, 'day': 5, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1484723091739-30a097e8f929?w=400&h=300&fit=crop'},

            {'title': 'Shawarma de pui cu cartofi', 'description': 'Pranz consistent si aromat.',
             'ingredients': '200g pui marinat, lipie mare, salata, rosii, sos usturoi, cartofi prajiti',
             'instructions': 'Grieleaza puiul. Asambleaza shawarma. Serveste cu cartofi.', 'calories': 820, 'day': 5, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400&h=300&fit=crop'},

            {'title': 'Lasagna cu carne', 'description': 'Cina clasica, bogata si satiosa.',
             'ingredients': 'foi lasagna, 200g vita tocata, bechamel, sos rosii, mozzarella',
             'instructions': 'Alternameaza straturile de paste, sos si branza. Coace 35 min la 180°C.', 'calories': 750, 'day': 5, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1551183053-bf91a1d81141?w=400&h=300&fit=crop'},

            {'title': 'Mix de nuci si ciocolata', 'description': 'Gustare energizanta.',
             'ingredients': '30g nuci caju, 20g ciocolata neagra, stafide',
             'instructions': 'Amesteca si savureaza.', 'calories': 320, 'day': 5, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1473093295043-cdd812d0e601?w=400&h=300&fit=crop'},


            # Sambata
            {'title': 'Oua Benedict cu bacon', 'description': 'Mic dejun de weekend premium.',
             'ingredients': '2 oua posat, 2 felii bacon, english muffin, sos hollandaise',
             'instructions': 'Posaza ouale. Prajeste baconul si muffinul. Asambleaza si pune sos.', 'calories': 620, 'day': 6, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=400&h=300&fit=crop'},

            {'title': 'Cotlet de porc cu piure si salata', 'description': 'Pranz substantial de weekend.',
             'ingredients': '200g cotlet porc, 250g cartofi, lapte, unt, salata verde',
             'instructions': 'Prajeste cotletul 5 min pe parte. Fa piure cremos. Serveste cu salata.', 'calories': 800, 'day': 6, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=400&h=300&fit=crop'},

            {'title': 'Pizza cu carne si branza', 'description': 'Cina de weekend generoasa.',
             'ingredients': 'blat pizza, sos rosii, mozzarella, sunca, salam, ardei, ciuperci',
             'instructions': 'Pregateste pizza cu toppinguri. Coace 12 min la 230°C.', 'calories': 750, 'day': 6, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=400&h=300&fit=crop'},

            {'title': 'Shake post-antrenament', 'description': 'Recuperare dupa efort.',
             'ingredients': '40g whey, 300ml lapte, banana, 30g ovaz',
             'instructions': 'Mixeaza totul si bea in 30 min dupa antrenament.', 'calories': 450, 'day': 6, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1505252585461-04db1eb84625?w=400&h=300&fit=crop'},


            # Duminica
            {'title': 'Pancakes americane cu sirop', 'description': 'Mic dejun festiv hipercaloric.',
             'ingredients': '100g faina, 2 oua, 150ml lapte, unt, sirop artar, afine',
             'instructions': 'Amesteca ingredientele. Prajeste clatitele in unt. Serveste cu sirop si fructe.', 'calories': 650, 'day': 7, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1567620905732-2d1ec7ab7445?w=400&h=300&fit=crop'},

            {'title': 'Rata cu cartofi la cuptor', 'description': 'Pranz festiv de duminica.',
             'ingredients': '200g piept rata, 250g cartofi, rozmarin, usturoi, ulei masline',
             'instructions': 'Condimenteaza rata. Coace impreuna cu cartofii 40 min la 190°C.', 'calories': 800, 'day': 7, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1558030006-450675393462?w=400&h=300&fit=crop'},

            {'title': 'Paste cu pesto si pui', 'description': 'Cina rapida si gustoasa.',
             'ingredients': '120g penne, 150g piept pui, pesto, rosii uscate, parmezan',
             'instructions': 'Fierbe pastele. Prajeste puiul. Amesteca totul cu pesto.', 'calories': 680, 'day': 7, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400&h=300&fit=crop'},

            {'title': 'Budinca de orez cu scortisoara', 'description': 'Desert nutritiv.',
             'ingredients': '80g orez, 300ml lapte, zahar, scortisoara, vanilie',
             'instructions': 'Fierbe orezul in lapte cu zahar si vanilie 25 min. Presara scortisoara.', 'calories': 380, 'day': 7, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1512058564366-18510be2db19?w=400&h=300&fit=crop'},

        ]
        for r in d3_recipes:
            Recipe.objects.get_or_create(diet=d3, title=r['title'], day=r['day'], defaults=r)

        # === DIETA 4: Indice glicemic scazut (insulina) ===
        d4, _ = Diet.objects.get_or_create(
            name='Plan cu Indice Glicemic Scazut',
            defaults={
                'goal': 'lose',
                'description': 'Plan special pentru persoane cu rezistenta la insulina. '
                               'Alimente cu IG scazut, bogate in fibre si proteine.',
                'calories_per_day': 1600,
                'is_insulin_friendly': True,
            }
        )
        d4_recipes = [
            # Luni
            {'title': 'Iaurt grecesc cu nuci si seminte chia', 'description': 'Mic dejun cu IG scazut si proteine.',
             'ingredients': '200g iaurt grecesc, 20g nuci, 10g seminte chia, cateva afine',
             'instructions': 'Pune iaurtul in bol, adauga nucile, semintele si afinele deasupra.', 'calories': 280, 'day': 1, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1488477181946-6428a0291777?w=400&h=300&fit=crop'},

            {'title': 'Salata cu ton si linte', 'description': 'Pranz bogat in fibre si proteine cu IG scazut.',
             'ingredients': '100g ton conserva, 80g linte fiarta, rosii, ceapa, ulei masline, lamaie',
             'instructions': 'Amesteca lintea cu tonul. Adauga legumele, uleiul si lamaia.', 'calories': 380, 'day': 1, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=400&h=300&fit=crop'},

            {'title': 'Pui cu legume la cuptor', 'description': 'Cina simpla cu carbohidrati minimi.',
             'ingredients': '150g pulpe pui dezosate, dovlecel, vinete, ardei, usturoi, ierburi',
             'instructions': 'Taie legumele, pune puiul deasupra. Condimenteaza si coace 35 min la 190°C.', 'calories': 350, 'day': 1, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400&h=300&fit=crop'},

            {'title': 'Telina cu hummus', 'description': 'Gustare cu fibre si proteine vegetale.',
             'ingredients': '3 tulpini telina, 40g hummus',
             'instructions': 'Taie telina batoane si serveste cu hummus.', 'calories': 110, 'day': 1, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1585937421612-70a008356fbe?w=400&h=300&fit=crop'},


            # Marti
            {'title': 'Omleta cu ciuperci si spanac', 'description': 'Mic dejun proteic fara carbohidrati.',
             'ingredients': '3 oua, 80g ciuperci, spanac, ulei masline',
             'instructions': 'Caleste ciupercile si spanacul. Adauga ouale batute. Gateste 4 min.', 'calories': 290, 'day': 2, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=400&h=300&fit=crop'},

            {'title': 'Peste cu salata de naut', 'description': 'Pranz mediteranean cu IG scazut.',
             'ingredients': '130g cod, 100g naut fiert, rosii, castravete, ceapa, patrunjel, lamaie',
             'instructions': 'Grieleaza pestele. Amesteca nautul cu legumele. Adauga lamaie.', 'calories': 400, 'day': 2, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=400&h=300&fit=crop'},

            {'title': 'Ghiveci de legume cu tofu', 'description': 'Cina vegetariana cu IG scazut.',
             'ingredients': '150g tofu, dovlecel, vinete, ardei, rosii, usturoi, busuioc',
             'instructions': 'Taie tofu si legumele. Caleste totul in ulei de masline 15 min.', 'calories': 300, 'day': 2, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1540420773420-3366772f4999?w=400&h=300&fit=crop'},

            {'title': 'Nuci si seminte', 'description': 'Gustare cu grasimi sanatoase.',
             'ingredients': '15g nuci, 10g seminte floarea soarelui, 10g seminte dovleac',
             'instructions': 'Amesteca si savureaza.', 'calories': 180, 'day': 2, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1473093295043-cdd812d0e601?w=400&h=300&fit=crop'},


            # Miercuri
            {'title': 'Budinca de chia cu cocos', 'description': 'Mic dejun preparat din seara anterioara.',
             'ingredients': '30g seminte chia, 200ml lapte cocos, vanilie, cateva zmeura',
             'instructions': 'Amesteca seara. Dimineata adauga fructele.', 'calories': 270, 'day': 3, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1488477181946-6428a0291777?w=400&h=300&fit=crop'},

            {'title': 'Suprem de curcan cu legume', 'description': 'Pranz proteic si satios.',
             'ingredients': '150g piept curcan, brocoli, conopida, morcov, usturoi, ulei masline',
             'instructions': 'Grieleaza curcanul. Gateste legumele la aburi. Adauga ulei si usturoi.', 'calories': 380, 'day': 3, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400&h=300&fit=crop'},

            {'title': 'Supa de linte rosie cu turmeric', 'description': 'Cina calda cu fibre si antiinflamatoare.',
             'ingredients': '100g linte rosie, turmeric, ghimbir, ceapa, usturoi, lamaie',
             'instructions': 'Caleste ceapa. Adauga lintea, condimentele si 500ml apa. Fierbe 18 min. Mixeaza.', 'calories': 310, 'day': 3, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1476718406336-bb5a9690ee2a?w=400&h=300&fit=crop'},

            {'title': 'Avocado cu lamaie si sare', 'description': 'Gustare cu grasimi mono-nesaturate.',
             'ingredients': '1/2 avocado, lamaie, sare de mare, fulgi chili',
             'instructions': 'Taie avocado si presara sare, lamaie si chili.', 'calories': 140, 'day': 3, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1525351484163-7529414344d8?w=400&h=300&fit=crop'},


            # Joi
            {'title': 'Oua fierte cu avocado', 'description': 'Mic dejun simplu cu grasimi bune.',
             'ingredients': '2 oua fierte, 1/2 avocado, sare, piper, rosie',
             'instructions': 'Fierbe ouale 8 min. Taie avocado si rosia. Serveste impreuna.', 'calories': 300, 'day': 4, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=400&h=300&fit=crop'},

            {'title': 'Wrap de salata cu pui', 'description': 'Pranz fara gluten si cu IG scazut.',
             'ingredients': 'frunze mari de salata, 130g pui grilat, castravete, morcov, sos tahini',
             'instructions': 'Pune puiul si legumele in frunzele de salata. Adauga sos tahini.', 'calories': 350, 'day': 4, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=400&h=300&fit=crop'},

            {'title': 'Cod cu sparanghel si lamaie', 'description': 'Cina usoara bogata in proteine.',
             'ingredients': '150g cod, sparanghel, lamaie, capere, ulei masline',
             'instructions': 'Coace codul si sparanghelul 15 min la 200°C. Stoarce lamaie deasupra.', 'calories': 300, 'day': 4, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1467003909585-2f8a72700288?w=400&h=300&fit=crop'},

            {'title': 'Castravete cu branza cottage', 'description': 'Gustare usoara si racoritoare.',
             'ingredients': '1 castravete, 80g branza cottage, marar',
             'instructions': 'Taie castravetele rondele, adauga branza si mararul.', 'calories': 100, 'day': 4, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1452195100486-9cc805987862?w=400&h=300&fit=crop'},


            # Vineri
            {'title': 'Smoothie verde cu avocado', 'description': 'Mic dejun cu grasimi bune si fibre.',
             'ingredients': '1/2 avocado, spanac, 200ml lapte migdale, lamaie, ghimbir',
             'instructions': 'Mixeaza totul 40 secunde.', 'calories': 250, 'day': 5, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1505252585461-04db1eb84625?w=400&h=300&fit=crop'},

            {'title': 'Salata cu somon si avocado', 'description': 'Pranz cu omega-3 si grasimi sanatoase.',
             'ingredients': '120g somon afumat, avocado, rucola, rosii, ulei masline, lamaie',
             'instructions': 'Aranjeaza rucola pe farfurie. Adauga somonul, avocado si rosiile. Drizzle ulei.', 'calories': 420, 'day': 5, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=400&h=300&fit=crop'},

            {'title': 'Dovlecei umpluti cu carne si legume', 'description': 'Cina cu putini carbohidrati.',
             'ingredients': '2 dovlecei, 120g carne tocata pui, ceapa, rosii, parmezan',
             'instructions': 'Scobeaza dovleceii. Caleste carnea cu legumele. Umple si coace 25 min.', 'calories': 320, 'day': 5, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1540420773420-3366772f4999?w=400&h=300&fit=crop'},

            {'title': 'Masline si branza feta', 'description': 'Gustare mediteraneana.',
             'ingredients': '8 masline, 30g feta, oregano',
             'instructions': 'Serveste impreuna cu un strop de ulei de masline.', 'calories': 150, 'day': 5, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1452195100486-9cc805987862?w=400&h=300&fit=crop'},


            # Sambata
            {'title': 'Clatite de cocos cu fructe', 'description': 'Mic dejun fara gluten si IG scazut.',
             'ingredients': '30g faina cocos, 2 oua, lapte cocos, capsuni, zmeura',
             'instructions': 'Amesteca faina, ouale si laptele. Prajeste clatitele. Adauga fructe.', 'calories': 290, 'day': 6, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1567620905732-2d1ec7ab7445?w=400&h=300&fit=crop'},

            {'title': 'Pui cu salata de quinoa', 'description': 'Pranz echilibrat cu cereale pseudo-integrale.',
             'ingredients': '140g pui, 60g quinoa, ardei, castravete, lamaie, menta',
             'instructions': 'Fierbe quinoa. Grieleaza puiul. Amesteca cu legumele si adauga lamaie.', 'calories': 400, 'day': 6, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=400&h=300&fit=crop'},

            {'title': 'Ciorba de fasole verde', 'description': 'Cina traditionala cu IG scazut.',
             'ingredients': 'fasole verde, morcov, ceapa, rosii, patrunjel, bors',
             'instructions': 'Fierbe legumele 20 min. Adauga borsul si verdeatza la final.', 'calories': 220, 'day': 6, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1476718406336-bb5a9690ee2a?w=400&h=300&fit=crop'},

            {'title': 'Ou fiert cu rosie', 'description': 'Gustare simpla si satiosa.',
             'ingredients': '1 ou fiert, 1 rosie, sare',
             'instructions': 'Fierbe oul. Taie rosia. Serveste cu sare.', 'calories': 110, 'day': 6, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=400&h=300&fit=crop'},


            # Duminica
            {'title': 'Frittata cu legume', 'description': 'Mic dejun de weekend cu IG scazut.',
             'ingredients': '3 oua, ardei, ceapa, spanac, branza de capra',
             'instructions': 'Caleste legumele. Adauga ouale batute. Gateste pe aragaz, apoi la cuptor 5 min.', 'calories': 310, 'day': 7, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=400&h=300&fit=crop'},

            {'title': 'Salata de pui cu nuci si mere', 'description': 'Pranz crocant si satios.',
             'ingredients': '140g pui, salata mixta, 1 mar verde, nuci, ulei masline',
             'instructions': 'Grieleaza puiul. Taie marul. Amesteca totul cu ulei si otet balsamic.', 'calories': 400, 'day': 7, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=400&h=300&fit=crop'},

            {'title': 'Curcan cu sos de mustar si legume', 'description': 'Cina aromatica si sanatoasa.',
             'ingredients': '150g piept curcan, mustar Dijon, smantana light, brocoli, morcov',
             'instructions': 'Grieleaza curcanul. Fa sosul din mustar si smantana. Serveste cu legume la aburi.', 'calories': 350, 'day': 7, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400&h=300&fit=crop'},

            {'title': 'Ardei umpluti cu branza', 'description': 'Gustare savuroasa si usoara.',
             'ingredients': '2 ardei mini, 50g branza cottage, marar, sare',
             'instructions': 'Taie ardeii si umple cu branza amestecata cu marar.', 'calories': 100, 'day': 7, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1452195100486-9cc805987862?w=400&h=300&fit=crop'},

        ]
        for r in d4_recipes:
            Recipe.objects.get_or_create(diet=d4, title=r['title'], day=r['day'], defaults=r)

        # === DIETA 5: Mediteraneana (mentinere) ===
        d5, _ = Diet.objects.get_or_create(
            name='Dieta Mediteraneana',
            defaults={
                'goal': 'maintain',
                'description': 'Inspirata din traditia culinara mediteraneana: ulei de masline, peste, '
                               'legume, fructe si cereale integrale. Ideala pentru sanatatea inimii.',
                'calories_per_day': 2000,
                'is_insulin_friendly': True,
            }
        )
        d5_recipes = [
            # Luni
            {'title': 'Paine cu rosii si ulei de masline', 'description': 'Pan con tomate - mic dejun spaniol.',
             'ingredients': '2 felii paine rustica, 1 rosie, ulei masline extravirgin, sare',
             'instructions': 'Prajeste painea. Rade rosia pe paine, stropeste cu ulei si adauga sare.', 'calories': 320, 'day': 1, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1484723091739-30a097e8f929?w=400&h=300&fit=crop'},

            {'title': 'Peste cu salata de naut', 'description': 'Pranz cu proteine si leguminoase.',
             'ingredients': '130g dorada, 100g naut, rosii, ceapa rosie, patrunjel, lamaie',
             'instructions': 'Grieleaza pestele. Amesteca nautul cu legumele. Adauga lamaie si ulei.', 'calories': 450, 'day': 1, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=400&h=300&fit=crop'},

            {'title': 'Salata greceasca cu feta', 'description': 'Cina clasica mediteraneana.',
             'ingredients': 'rosii, castravete, ardei, ceapa, masline kalamata, feta, oregano, ulei masline',
             'instructions': 'Taie legumele bucati mari. Adauga feta, masline, oregano si ulei generos.', 'calories': 380, 'day': 1, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=400&h=300&fit=crop'},

            {'title': 'Smochine cu ricotta si miere', 'description': 'Gustare eleganta si nutritiva.',
             'ingredients': '3 smochine, 50g ricotta, miere, nuci',
             'instructions': 'Taie smochinele, umple cu ricotta. Adauga miere si nuci.', 'calories': 200, 'day': 1, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1490474418585-ba9bad8fd0ea?w=400&h=300&fit=crop'},


            # Marti
            {'title': 'Iaurt cu fructe si migdale', 'description': 'Mic dejun simplu si sanatos.',
             'ingredients': '200g iaurt grecesc, piersica, 15g migdale, miere',
             'instructions': 'Taie piersica. Adauga iaurtul, migdalele si un fir de miere.', 'calories': 300, 'day': 2, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1488477181946-6428a0291777?w=400&h=300&fit=crop'},

            {'title': 'Risotto cu fructe de mare', 'description': 'Pranz italian clasic.',
             'ingredients': '80g orez, 150g mix fructe de mare, vin alb, usturoi, patrunjel',
             'instructions': 'Caleste usturoiul, adauga orezul si vinul. Pune supa treptat. Adauga fructele de mare.', 'calories': 520, 'day': 2, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1476124369491-e7addf5db371?w=400&h=300&fit=crop'},

            {'title': 'Bruschette cu rosii si busuioc', 'description': 'Cina usoara in stil italian.',
             'ingredients': 'paine ciabatta, rosii, busuioc, usturoi, ulei masline, otet balsamic',
             'instructions': 'Prajeste painea. Toaca rosiile cu busuioc si usturoi. Pune deasupra painii.', 'calories': 350, 'day': 2, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1484723091739-30a097e8f929?w=400&h=300&fit=crop'},

            {'title': 'Masline si migdale', 'description': 'Gustare mediteraneana clasica.',
             'ingredients': '10 masline kalamata, 15g migdale',
             'instructions': 'Serveste ca atare.', 'calories': 170, 'day': 2, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1473093295043-cdd812d0e601?w=400&h=300&fit=crop'},


            # Miercuri
            {'title': 'Omleta cu rosii uscate si feta', 'description': 'Mic dejun mediteranean.',
             'ingredients': '3 oua, rosii uscate, feta, busuioc, ulei masline',
             'instructions': 'Bate ouale, adauga rosiile si feta. Gateste in ulei de masline.', 'calories': 350, 'day': 3, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=400&h=300&fit=crop'},

            {'title': 'Calamari la gratar cu salata', 'description': 'Pranz usor cu fructe de mare.',
             'ingredients': '150g calamari, salata mixta, rosii, masline, lamaie',
             'instructions': 'Grieleaza calamarii 2 min pe parte. Serveste cu salata si lamaie.', 'calories': 380, 'day': 3, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=400&h=300&fit=crop'},

            {'title': 'Paste cu sos de rosii proaspete', 'description': 'Cina simpla si autentica.',
             'ingredients': '100g spaghetti, rosii proaspete, usturoi, busuioc, ulei masline, parmezan',
             'instructions': 'Fierbe pastele. Caleste usturoiul, adauga rosiile. Combina cu parmezan.', 'calories': 450, 'day': 3, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1551183053-bf91a1d81141?w=400&h=300&fit=crop'},

            {'title': 'Hummus cu paine pita', 'description': 'Gustare din orientul mijlociu.',
             'ingredients': '50g hummus, 1/2 paine pita integrala',
             'instructions': 'Taie pita felii si serveste cu hummus.', 'calories': 180, 'day': 3, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1585937421612-70a008356fbe?w=400&h=300&fit=crop'},


            # Joi
            {'title': 'Shakshuka (oua in sos de rosii)', 'description': 'Mic dejun nord-african clasic.',
             'ingredients': '2 oua, rosii, ardei, ceapa, usturoi, boia, chimion, patrunjel',
             'instructions': 'Caleste legumele, adauga rosiile. Sparge ouale deasupra. Acopera 5 min.', 'calories': 320, 'day': 4, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=400&h=300&fit=crop'},

            {'title': 'Somon cu sos de lamaie si capere', 'description': 'Pranz elegant si sanatos.',
             'ingredients': '140g somon, lamaie, capere, unt, ierburi proaspete',
             'instructions': 'Prajeste somonul 4 min pe parte. Fa sosul din unt, lamaie si capere.', 'calories': 480, 'day': 4, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1467003909585-2f8a72700288?w=400&h=300&fit=crop'},

            {'title': 'Tabouleh cu bulgur', 'description': 'Salata libaneza de cina.',
             'ingredients': '60g bulgur, patrunjel, menta, rosii, castravete, lamaie, ulei masline',
             'instructions': 'Fierbe bulgur 10 min. Toaca verdeatza si legumele. Amesteca totul.', 'calories': 350, 'day': 4, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=400&h=300&fit=crop'},

            {'title': 'Struguri si branza', 'description': 'Gustare clasica mediteraneana.',
             'ingredients': '100g struguri, 30g branza brie',
             'instructions': 'Serveste impreuna.', 'calories': 180, 'day': 4, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1452195100486-9cc805987862?w=400&h=300&fit=crop'},


            # Vineri
            {'title': 'Paine cu avocado si lamaie', 'description': 'Mic dejun rapid si satios.',
             'ingredients': '1 felie paine integrala, 1/2 avocado, lamaie, fulgi chili, sare',
             'instructions': 'Zdrobeste avocado pe paine. Adauga lamaie si condimente.', 'calories': 280, 'day': 5, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1525351484163-7529414344d8?w=400&h=300&fit=crop'},

            {'title': 'Paella cu pui si legume', 'description': 'Pranz spaniol festiv.',
             'ingredients': '100g orez, 120g pui, ardei, mazare, sofran, rosii, stoc pui',
             'instructions': 'Prajeste puiul, adauga orezul si stocul. Gateste 20 min fara sa amesteci.', 'calories': 530, 'day': 5, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400&h=300&fit=crop'},

            {'title': 'Creveti cu usturoi si lamaie', 'description': 'Cina rapida si gustoasa.',
             'ingredients': '150g creveti, usturoi, vin alb, lamaie, patrunjel, ulei masline',
             'instructions': 'Caleste usturoiul in ulei. Adauga crevetii si vinul. Gateste 3 min.', 'calories': 320, 'day': 5, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1565958011703-44f9829ba187?w=400&h=300&fit=crop'},

            {'title': 'Portocala si nuci', 'description': 'Gustare cu vitamina C.',
             'ingredients': '1 portocala, 15g nuci',
             'instructions': 'Curata portocala si serveste cu nucile.', 'calories': 160, 'day': 5, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1473093295043-cdd812d0e601?w=400&h=300&fit=crop'},


            # Sambata
            {'title': 'Frittata cu legume', 'description': 'Mic dejun de weekend la cuptor.',
             'ingredients': '3 oua, dovlecel, ardei, ceapa, masline, feta',
             'instructions': 'Caleste legumele. Adauga ouale. Pune la cuptor 10 min.', 'calories': 340, 'day': 6, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=400&h=300&fit=crop'},

            {'title': 'Peste intreg la cuptor cu ierburi', 'description': 'Pranz festiv de weekend.',
             'ingredients': '1 dorada, lamaie, rozmarin, usturoi, rosii, cartofi noi',
             'instructions': 'Umple pestele cu lamaie si ierburi. Coace cu cartofi 30 min la 200°C.', 'calories': 520, 'day': 6, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1467003909585-2f8a72700288?w=400&h=300&fit=crop'},

            {'title': 'Minestrone italian', 'description': 'Supa densa de legume pt cina.',
             'ingredients': 'fasole, paste mici, morcov, telina, dovlecel, rosii, busuioc',
             'instructions': 'Fierbe legumele 20 min. Adauga pastele si fierbe inca 8 min. Adauga busuioc.', 'calories': 380, 'day': 6, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1476718406336-bb5a9690ee2a?w=400&h=300&fit=crop'},

            {'title': 'Bruschetta cu rosii', 'description': 'Gustare usoara de seara.',
             'ingredients': '1 felie paine, rosii, busuioc, ulei masline',
             'instructions': 'Prajeste painea, adauga rosiile taiate si busuiocul.', 'calories': 150, 'day': 6, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1484723091739-30a097e8f929?w=400&h=300&fit=crop'},


            # Duminica
            {'title': 'Focaccia cu rosii si oregano', 'description': 'Mic dejun italian de weekend.',
             'ingredients': '1 felie focaccia, rosii cherry, oregano, ulei masline',
             'instructions': 'Incalzeste focaccia, adauga rosii si oregano.', 'calories': 350, 'day': 7, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=400&h=300&fit=crop'},

            {'title': 'Musaca usoara cu vinete', 'description': 'Pranz mediteranean traditional.',
             'ingredients': '2 vinete, 150g carne tocata, sos rosii, bechamel light, parmezan',
             'instructions': 'Taie si coace vinetele. Alternameaza cu carne si sos. Coace 30 min.', 'calories': 520, 'day': 7, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1540189549336-e6e99c3679fe?w=400&h=300&fit=crop'},

            {'title': 'Salata cu halloumi la gratar', 'description': 'Cina usoara de duminica seara.',
             'ingredients': '100g halloumi, rosii, castravete, rucola, masline, ulei masline',
             'instructions': 'Grieleaza halloumi 2 min pe parte. Serveste pe salata.', 'calories': 380, 'day': 7, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=400&h=300&fit=crop'},

            {'title': 'Pere cu branza de capra si miere', 'description': 'Desert mediteranean.',
             'ingredients': '1 para, 30g branza capra, miere, nuci',
             'instructions': 'Taie para, adauga branza, nuci si un fir de miere.', 'calories': 180, 'day': 7, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1490474418585-ba9bad8fd0ea?w=400&h=300&fit=crop'},

        ]
        for r in d5_recipes:
            Recipe.objects.get_or_create(diet=d5, title=r['title'], day=r['day'], defaults=r)

        # === DIETA 6: Vegetariana echilibrata (mentinere) ===
        d6, _ = Diet.objects.get_or_create(
            name='Vegetariana Echilibrata',
            defaults={
                'goal': 'maintain',
                'description': 'Plan vegetarian complet, cu suficiente proteine din leguminoase, '
                               'oua, lactate si cereale. Potrivit si pentru cei care vor sa reduca carnea.',
                'calories_per_day': 1900,
                'is_insulin_friendly': False,
            }
        )
        d6_recipes = [
            # Luni
            {'title': 'Ovaz cu fructe de padure si seminte', 'description': 'Mic dejun cu fibre si antioxidanti.',
             'ingredients': '60g fulgi ovaz, 200ml lapte, afine, zmeura, seminte in, miere',
             'instructions': 'Fierbe ovazul in lapte. Adauga fructele, semintele si mierea.', 'calories': 380, 'day': 1, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1490474418585-ba9bad8fd0ea?w=400&h=300&fit=crop'},

            {'title': 'Curry de naut cu orez', 'description': 'Pranz satios cu proteine vegetale.',
             'ingredients': '150g naut, lapte cocos, pasta curry, spanac, rosii, 80g orez',
             'instructions': 'Gateste curryul 15 min. Fierbe orezul separat.', 'calories': 520, 'day': 1, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1512058564366-18510be2db19?w=400&h=300&fit=crop'},

            {'title': 'Paste primavera cu legume', 'description': 'Cina usoara si colorata.',
             'ingredients': '100g penne, dovlecel, ardei, rosii cherry, busuioc, parmezan',
             'instructions': 'Fierbe pastele. Caleste legumele. Combina cu parmezan.', 'calories': 450, 'day': 1, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1551183053-bf91a1d81141?w=400&h=300&fit=crop'},

            {'title': 'Hummus cu morcovi', 'description': 'Gustare crocanta si proteica.',
             'ingredients': '50g hummus, 2 morcovi',
             'instructions': 'Taie morcovii batoane si serveste cu hummus.', 'calories': 160, 'day': 1, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1585937421612-70a008356fbe?w=400&h=300&fit=crop'},


            # Marti
            {'title': 'Toast cu avocado si ou posat', 'description': 'Mic dejun trendy si nutritiv.',
             'ingredients': '1 felie paine integrala, 1/2 avocado, 1 ou, fulgi chili',
             'instructions': 'Prajeste painea. Intinde avocado. Adauga oul posat si chili.', 'calories': 350, 'day': 2, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=400&h=300&fit=crop'},

            {'title': 'Salata de linte cu branza feta', 'description': 'Pranz bogat in fibre si proteine.',
             'ingredients': '100g linte verde, feta, rosii uscate, rucola, ceapa rosie, lamaie',
             'instructions': 'Fierbe lintea. Amesteca cu legumele si feta. Drizzle lamaie.', 'calories': 430, 'day': 2, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=400&h=300&fit=crop'},

            {'title': 'Omleta cu legume si branza', 'description': 'Cina rapida si satioasa.',
             'ingredients': '3 oua, ardei, ciuperci, spanac, cascaval',
             'instructions': 'Caleste legumele. Adauga ouale. Presara cascavalul si gateste.', 'calories': 380, 'day': 2, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=400&h=300&fit=crop'},

            {'title': 'Mar cu unt de migdale', 'description': 'Gustare cu grasimi sanatoase.',
             'ingredients': '1 mar, 15g unt migdale',
             'instructions': 'Taie marul si unge feliile cu unt de migdale.', 'calories': 170, 'day': 2, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1490474418585-ba9bad8fd0ea?w=400&h=300&fit=crop'},


            # Miercuri
            {'title': 'Smoothie bowl tropical', 'description': 'Mic dejun colorat si racoritor.',
             'ingredients': 'mango, banana, lapte cocos, granola, seminte chia, cocos razuit',
             'instructions': 'Mixeaza mango si banana cu lapte. Pune in bol si decoreaza cu toppinguri.', 'calories': 400, 'day': 3, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1505252585461-04db1eb84625?w=400&h=300&fit=crop'},

            {'title': 'Supa crema de mazare cu menta', 'description': 'Pranz cald si reconfortant.',
             'ingredients': '200g mazare, ceapa, usturoi, stoc legume, menta, smantana',
             'instructions': 'Caleste ceapa. Adauga mazarea si stocul. Fierbe 10 min. Mixeaza cu menta.', 'calories': 350, 'day': 3, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1476718406336-bb5a9690ee2a?w=400&h=300&fit=crop'},

            {'title': 'Quesadilla cu fasole si porumb', 'description': 'Cina mexicana vegetariana.',
             'ingredients': '2 tortillas, fasole neagra, porumb, ardei, cascaval, smantana',
             'instructions': 'Umple tortillele cu ingredientele. Prajeste pe ambele parti.', 'calories': 480, 'day': 3, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1626700051175-6818013e1d4f?w=400&h=300&fit=crop'},

            {'title': 'Edamame cu sare', 'description': 'Gustare proteica din soia.',
             'ingredients': '100g edamame, sare de mare',
             'instructions': 'Fierbe edamame 5 min. Adauga sare.', 'calories': 120, 'day': 3, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1540420773420-3366772f4999?w=400&h=300&fit=crop'},


            # Joi
            {'title': 'Clatite cu ricotta si lamaie', 'description': 'Mic dejun fin si proteic.',
             'ingredients': '100g ricotta, 2 oua, 30g faina, coaja lamaie, afine',
             'instructions': 'Amesteca ricotta cu ouale si faina. Prajeste. Adauga afine.', 'calories': 370, 'day': 4, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1567620905732-2d1ec7ab7445?w=400&h=300&fit=crop'},

            {'title': 'Buddha bowl cu tofu si quinoa', 'description': 'Pranz complet si colorat.',
             'ingredients': '100g tofu, 60g quinoa, edamame, morcov, avocado, varza rosie, sos tahini',
             'instructions': 'Prajeste tofu. Fierbe quinoa. Aranjeaza totul in bol cu sos.', 'calories': 500, 'day': 4, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1512058564366-18510be2db19?w=400&h=300&fit=crop'},

            {'title': 'Gratin de conopida', 'description': 'Cina calda gratinata la cuptor.',
             'ingredients': 'conopida, bechamel, cascaval, nucsoara, piper',
             'instructions': 'Fierbe conopida. Pune in tava cu sos bechamel si cascaval. Gratineaza 15 min.', 'calories': 380, 'day': 4, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1540420773420-3366772f4999?w=400&h=300&fit=crop'},

            {'title': 'Banana congelata cu ciocolata', 'description': 'Gustare desert sanatoasa.',
             'ingredients': '1 banana, 15g ciocolata neagra topita',
             'instructions': 'Taie banana, inmoaie in ciocolata. Congeleaza 1 ora.', 'calories': 170, 'day': 4, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1490474418585-ba9bad8fd0ea?w=400&h=300&fit=crop'},


            # Vineri
            {'title': 'Granola cu iaurt si kiwi', 'description': 'Mic dejun crocant si acrisor.',
             'ingredients': '150g iaurt, 30g granola, 1 kiwi, miere',
             'instructions': 'Pune iaurtul, presara granola si adauga kiwi feliat.', 'calories': 320, 'day': 5, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1488477181946-6428a0291777?w=400&h=300&fit=crop'},

            {'title': 'Wrap cu falafel si hummus', 'description': 'Pranz oriental vegetarian.',
             'ingredients': '3 falafel, lipie integrala, hummus, salata, rosii, sos tahini',
             'instructions': 'Incalzeste falafelul. Asambleaza in lipie cu toate ingredientele.', 'calories': 500, 'day': 5, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1626700051175-6818013e1d4f?w=400&h=300&fit=crop'},

            {'title': 'Risotto cu ciuperci si trufe', 'description': 'Cina eleganta de vineri.',
             'ingredients': '80g orez arborio, 150g ciuperci, ulei trufe, parmezan, ceapa',
             'instructions': 'Caleste ceapa. Adauga orezul. Pune supa treptat. Incorporeaza ciupercile si uleiul.', 'calories': 460, 'day': 5, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1476124369491-e7addf5db371?w=400&h=300&fit=crop'},

            {'title': 'Fructe uscate si nuci', 'description': 'Gustare energizanta.',
             'ingredients': '20g caise uscate, 15g nuci caju, 10g stafide',
             'instructions': 'Amesteca si savureaza.', 'calories': 180, 'day': 5, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1490474418585-ba9bad8fd0ea?w=400&h=300&fit=crop'},


            # Sambata
            {'title': 'Pancakes cu afine si sirop', 'description': 'Mic dejun festiv de weekend.',
             'ingredients': '80g faina integrala, 1 ou, 150ml lapte, afine, sirop artar',
             'instructions': 'Amesteca aluatul. Prajeste in tigaie. Serveste cu afine si sirop.', 'calories': 420, 'day': 6, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1567620905732-2d1ec7ab7445?w=400&h=300&fit=crop'},

            {'title': 'Pizza margherita cu blat subtire', 'description': 'Pranz clasic vegetarian.',
             'ingredients': 'blat pizza, sos rosii, mozzarella proaspata, busuioc, ulei masline',
             'instructions': 'Intinde sosul, adauga mozzarella. Coace 10 min la 230°C. Busuioc la sfarsit.', 'calories': 520, 'day': 6, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=400&h=300&fit=crop'},

            {'title': 'Supa de linte cu lamaie', 'description': 'Cina calda si reconfortanta.',
             'ingredients': '100g linte rosie, morcov, ceapa, lamaie, coriandru',
             'instructions': 'Fierbe lintea cu legumele 18 min. Stoarce lamaie. Adauga coriandru.', 'calories': 340, 'day': 6, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1476718406336-bb5a9690ee2a?w=400&h=300&fit=crop'},

            {'title': 'Tortilla chips cu guacamole', 'description': 'Gustare de seara mexicana.',
             'ingredients': 'tortilla chips, 1/2 avocado, lamaie, rosie, coriandru',
             'instructions': 'Fa guacamole. Serveste cu chips.', 'calories': 200, 'day': 6, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1525351484163-7529414344d8?w=400&h=300&fit=crop'},


            # Duminica
            {'title': 'Briosa de oua cu spanac si branza', 'description': 'Mic dejun pregatit la cuptor.',
             'ingredients': '4 oua, spanac, branza feta, ceapa verde, rosii uscate',
             'instructions': 'Bate ouale. Adauga ingredientele. Pune in forme. Coace 20 min la 180°C.', 'calories': 340, 'day': 7, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=400&h=300&fit=crop'},

            {'title': 'Lasagna vegetariana cu spanac', 'description': 'Pranz festiv de duminica.',
             'ingredients': 'foi lasagna, spanac, ricotta, mozzarella, sos rosii, parmezan',
             'instructions': 'Alternameaza straturile. Coace 35 min la 180°C.', 'calories': 540, 'day': 7, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1551183053-bf91a1d81141?w=400&h=300&fit=crop'},

            {'title': 'Salata calda de cartofi si fasole', 'description': 'Cina usoara si satiosa.',
             'ingredients': 'cartofi noi, fasole verde, ou fiert, mustar, ulei masline',
             'instructions': 'Fierbe cartofii si fasolea. Amesteca cu dressing de mustar si ulei.', 'calories': 400, 'day': 7, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=400&h=300&fit=crop'},

            {'title': 'Smoothie cu mango si cocos', 'description': 'Gustare tropicala racoritoare.',
             'ingredients': '100g mango, 150ml lapte cocos, gheata',
             'instructions': 'Mixeaza totul 30 secunde.', 'calories': 170, 'day': 7, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1505252585461-04db1eb84625?w=400&h=300&fit=crop'},

        ]
        for r in d6_recipes:
            Recipe.objects.get_or_create(diet=d6, title=r['title'], day=r['day'], defaults=r)

        # === DIETA 7: Keto / Low Carb (slabire) ===
        d7, _ = Diet.objects.get_or_create(
            name='Keto - Low Carb',
            defaults={
                'goal': 'lose',
                'description': 'Plan alimentar cu carbohidrati foarte redusi (sub 50g/zi) si grasimi crescute. '
                               'Induce cetoza - corpul arde grasimile ca sursa principala de energie.',
                'calories_per_day': 1700,
                'is_insulin_friendly': True,
            }
        )
        d7_recipes = [
            # Luni
            {'title': 'Oua cu bacon si avocado', 'description': 'Mic dejun keto clasic.',
             'ingredients': '3 oua, 2 felii bacon, 1/2 avocado, sare, piper',
             'instructions': 'Prajeste baconul. Gateste ouale in grasimea ramasa. Serveste cu avocado.', 'calories': 480, 'day': 1, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=400&h=300&fit=crop'},

            {'title': 'Salata cu pui si dressing ranch', 'description': 'Pranz bogat in grasimi sanatoase.',
             'ingredients': '150g pui grilat, salata, avocado, bacon crocant, dressing ranch, rosii',
             'instructions': 'Grieleaza puiul. Amesteca cu salata si toppingurile. Adauga dressing.', 'calories': 520, 'day': 1, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=400&h=300&fit=crop'},

            {'title': 'Steak cu unt si sparanghel', 'description': 'Cina consistenta fara carbohidrati.',
             'ingredients': '180g steak vita, 20g unt, sparanghel, usturoi',
             'instructions': 'Gateste steakul in unt 4 min/parte. Salteza sparanghelul in aceeasi tigaie.', 'calories': 520, 'day': 1, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1558030006-450675393462?w=400&h=300&fit=crop'},

            {'title': 'Branza cu masline', 'description': 'Gustare keto rapida.',
             'ingredients': '40g branza cheddar, 8 masline',
             'instructions': 'Serveste asa cum sunt.', 'calories': 200, 'day': 1, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1452195100486-9cc805987862?w=400&h=300&fit=crop'},


            # Marti
            {'title': 'Omleta cu branza si avocado', 'description': 'Mic dejun satios si low-carb.',
             'ingredients': '3 oua, 30g branza cheddar, 1/2 avocado, ceapa verde',
             'instructions': 'Bate ouale, adauga branza. Gateste si serveste cu avocado.', 'calories': 460, 'day': 2, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=400&h=300&fit=crop'},

            {'title': 'Somon cu sos de unt si lamaie', 'description': 'Pranz bogat in omega-3.',
             'ingredients': '150g somon, unt, lamaie, capere, salata verde',
             'instructions': 'Prajeste somonul. Fa sosul din unt topit cu lamaie si capere.', 'calories': 500, 'day': 2, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1467003909585-2f8a72700288?w=400&h=300&fit=crop'},

            {'title': 'Pui in sos cremos cu ciuperci', 'description': 'Cina cremoasa si satiosa.',
             'ingredients': '150g piept pui, 100g ciuperci, smantana, usturoi, parmezan',
             'instructions': 'Prajeste puiul. Caleste ciupercile. Adauga smantana si parmezanul.', 'calories': 480, 'day': 2, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400&h=300&fit=crop'},

            {'title': 'Ou fiert cu maioneza', 'description': 'Gustare rapida keto.',
             'ingredients': '2 oua fierte, 15g maioneza, boia',
             'instructions': 'Fierbe ouale. Taie si adauga maioneza si boia.', 'calories': 220, 'day': 2, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=400&h=300&fit=crop'},


            # Miercuri
            {'title': 'Clatite keto cu branza', 'description': 'Mic dejun cu faina de migdale.',
             'ingredients': '30g faina migdale, 2 oua, 50g branza crema, scortisoara',
             'instructions': 'Amesteca totul. Prajeste clatitele mici pe ambele parti.', 'calories': 380, 'day': 3, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1567620905732-2d1ec7ab7445?w=400&h=300&fit=crop'},

            {'title': 'Burger fara chifla cu salata', 'description': 'Pranz keto clasic.',
             'ingredients': '180g vita tocata, salata, rosie, castravete, cascaval, mustar, maioneza',
             'instructions': 'Grieleaza burgerul. Serveste pe pat de salata cu condimente.', 'calories': 520, 'day': 3, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=400&h=300&fit=crop'},

            {'title': 'Cotlet de porc cu brocoli si unt', 'description': 'Cina substatiala keto.',
             'ingredients': '180g cotlet porc, brocoli, unt, usturoi, lamaie',
             'instructions': 'Prajeste cotletul 5 min pe parte. Salteza brocoli in unt cu usturoi.', 'calories': 500, 'day': 3, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1558030006-450675393462?w=400&h=300&fit=crop'},

            {'title': 'Migdale si ciocolata neagra', 'description': 'Gustare cu grasimi bune.',
             'ingredients': '20g migdale, 15g ciocolata neagra 85%',
             'instructions': 'Savureaza lent.', 'calories': 200, 'day': 3, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1473093295043-cdd812d0e601?w=400&h=300&fit=crop'},


            # Joi
            {'title': 'Scrambled eggs cu smoked salmon', 'description': 'Mic dejun premium keto.',
             'ingredients': '3 oua, 60g somon afumat, unt, ceapa verde, branza crema',
             'instructions': 'Scramble ouale in unt la foc mic. Adauga somonul si branza.', 'calories': 450, 'day': 4, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=400&h=300&fit=crop'},

            {'title': 'Salata Caesar fara crutoane', 'description': 'Pranz clasic adaptat keto.',
             'ingredients': '150g pui, salata romana, parmezan, dressing Caesar, bacon',
             'instructions': 'Grieleaza puiul. Amesteca cu salata, parmezan si dressing.', 'calories': 480, 'day': 4, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=400&h=300&fit=crop'},

            {'title': 'Pulpe de pui cu sos pesto', 'description': 'Cina aromatica low-carb.',
             'ingredients': '2 pulpe pui, pesto, mozzarella, rosii, salata',
             'instructions': 'Coace pulpele 30 min. Adauga pesto si mozzarella in ultimele 5 min.', 'calories': 520, 'day': 4, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400&h=300&fit=crop'},

            {'title': 'Guacamole cu telina', 'description': 'Gustare crocanta si cremoasa.',
             'ingredients': '1/2 avocado, lamaie, ceapa, 3 tulpini telina',
             'instructions': 'Fa guacamole si serveste cu telina.', 'calories': 170, 'day': 4, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1525351484163-7529414344d8?w=400&h=300&fit=crop'},


            # Vineri
            {'title': 'Smoothie keto cu cocos', 'description': 'Mic dejun lichid cu grasimi MCT.',
             'ingredients': '200ml lapte cocos, 1/2 avocado, 15g ulei cocos, cacao, stevia',
             'instructions': 'Mixeaza totul 30 secunde.', 'calories': 400, 'day': 5, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1505252585461-04db1eb84625?w=400&h=300&fit=crop'},

            {'title': 'Creveti cu unt si usturoi', 'description': 'Pranz rapid si delicios.',
             'ingredients': '200g creveti, unt, usturoi, lamaie, patrunjel, ardei iute',
             'instructions': 'Topeste untul, adauga usturoiul si crevetii. Gateste 3 min.', 'calories': 450, 'day': 5, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1565958011703-44f9829ba187?w=400&h=300&fit=crop'},

            {'title': 'Vita cu sos gorgonzola', 'description': 'Cina premium keto.',
             'ingredients': '180g steak, 50g gorgonzola, smantana, nuci, salata',
             'instructions': 'Gateste steakul. Topeste gorgonzola cu smantana. Serveste deasupra.', 'calories': 580, 'day': 5, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1558030006-450675393462?w=400&h=300&fit=crop'},

            {'title': 'Castraveti cu branza crema', 'description': 'Gustare usoara si racoritoare.',
             'ingredients': '1 castravete, 40g branza crema, marar',
             'instructions': 'Taie castravetele rondele. Adauga branza si marar.', 'calories': 120, 'day': 5, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1452195100486-9cc805987862?w=400&h=300&fit=crop'},


            # Sambata
            {'title': 'Waffle keto cu frisca', 'description': 'Mic dejun de weekend special.',
             'ingredients': '30g faina migdale, 2 oua, branza crema, frisca, capsuni',
             'instructions': 'Amesteca ingredientele. Gateste la aparatul de waffle. Serveste cu frisca.', 'calories': 420, 'day': 6, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1562376552-0d160a2f238d?w=400&h=300&fit=crop'},

            {'title': 'Salata nicoise keto', 'description': 'Pranz frantuzesc adaptat.',
             'ingredients': '100g ton, ou fiert, masline, fasole verde, rosii, ansoa, ulei masline',
             'instructions': 'Fierbe oul si fasolea. Aranjeaza totul pe farfurie. Adauga ulei.', 'calories': 480, 'day': 6, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=400&h=300&fit=crop'},

            {'title': 'Rata cu varza rosie calda', 'description': 'Cina festiva low-carb.',
             'ingredients': '180g piept rata, varza rosie, mar, otet, unt',
             'instructions': 'Gateste rata in tigaie. Caleste varza cu mar si otet 20 min.', 'calories': 520, 'day': 6, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1558030006-450675393462?w=400&h=300&fit=crop'},

            {'title': 'Fat bombs cu ciocolata', 'description': 'Gustare keto cu energie concentrata.',
             'ingredients': '15g unt cocos, 10g cacao, 10g unt arahide, stevia',
             'instructions': 'Topeste si amesteca. Pune in forme. Congeleaza 30 min.', 'calories': 180, 'day': 6, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1497888329096-51c27beff665?w=400&h=300&fit=crop'},


            # Duminica
            {'title': 'Brunch keto: bacon, oua, avocado', 'description': 'Mic dejun complet de duminica.',
             'ingredients': '3 oua, 3 felii bacon, 1 avocado intreg, rosii cherry',
             'instructions': 'Prajeste baconul si ouale. Taie avocado. Serveste totul pe o platou.', 'calories': 580, 'day': 7, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=400&h=300&fit=crop'},

            {'title': 'Pui cu mozzarella si rosii la cuptor', 'description': 'Pranz simplu si gustos.',
             'ingredients': '2 piepturi pui, mozzarella, rosii, busuioc, ulei masline',
             'instructions': 'Pune puiul in tava. Adauga rosii, mozzarella si busuioc. Coace 25 min.', 'calories': 480, 'day': 7, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400&h=300&fit=crop'},

            {'title': 'Somon cu sparanghel in unt', 'description': 'Cina keto de duminica seara.',
             'ingredients': '140g somon, sparanghel, unt, lamaie, marar',
             'instructions': 'Gateste somonul si sparanghelul in unt. Stoarce lamaie si adauga marar.', 'calories': 460, 'day': 7, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1467003909585-2f8a72700288?w=400&h=300&fit=crop'},

            {'title': 'Branza brie cu nuci', 'description': 'Gustare eleganta keto.',
             'ingredients': '40g brie, 15g nuci pecan',
             'instructions': 'Serveste impreuna.', 'calories': 210, 'day': 7, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1473093295043-cdd812d0e601?w=400&h=300&fit=crop'},

        ]
        for r in d7_recipes:
            Recipe.objects.get_or_create(diet=d7, title=r['title'], day=r['day'], defaults=r)

        # === DIETA 8: Plan Flexibil de Mentinere ===
        d8, _ = Diet.objects.get_or_create(
            name='Plan Flexibil de Mentinere',
            defaults={
                'goal': 'maintain',
                'description': 'Plan alimentar echilibrat bazat pe principiul 80/20. Mese nutritive cu flexibilitate '
                               'pentru gusturi variate. Ideal pentru cei care vor sa mentina greutatea fara restrictii severe.',
                'calories_per_day': 2100,
                'is_insulin_friendly': False,
            }
        )
        d8_recipes = [
            # Luni
            {'title': 'Budinca de ovaz cu banane', 'description': 'Mic dejun cremos pregatit din seara precedenta.',
             'ingredients': '60g ovaz, 200ml lapte, 1 banana, scortisoara, miere, seminte chia',
             'instructions': 'Amesteca ovazul cu laptele si semintele chia. Lasa la frigider peste noapte. Dimineata adauga banana si miere.', 'calories': 380, 'day': 1, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1517673400267-0251440c45dc?w=400&h=300&fit=crop'},
            {'title': 'Wrap cu pui si legume', 'description': 'Pranz rapid si satios, usor de luat la pachet.',
             'ingredients': '1 tortilla integrala, 120g pui la gratar, salata, rosii, castravete, iaurt grecesc',
             'instructions': 'Grieleaza puiul. Intinde iaurtul pe tortilla. Adauga puiul si legumele. Ruleaza strans.', 'calories': 480, 'day': 1, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1626700051175-6818013e1d4f?w=400&h=300&fit=crop'},
            {'title': 'Paste integrale cu sos de rosii si busuioc', 'description': 'Cina clasica italiana, simpla si gustoasa.',
             'ingredients': '80g paste integrale, 200g rosii pasate, usturoi, busuioc, parmezan, ulei masline',
             'instructions': 'Fierbe pastele. Caleste usturoiul, adauga rosiile, gateste 10 min. Amesteca pastele cu sosul si presara parmezan.', 'calories': 450, 'day': 1, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1621996346565-e3dbc646d9a9?w=400&h=300&fit=crop'},
            {'title': 'Banana cu unt de arahide', 'description': 'Gustare energizanta rapida.',
             'ingredients': '1 banana, 20g unt de arahide',
             'instructions': 'Taie banana si adauga untul de arahide.', 'calories': 220, 'day': 1, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1490474418585-ba9bad8fd0ea?w=400&h=300&fit=crop'},

            # Marti
            {'title': 'Sandwich cu ou si avocado', 'description': 'Mic dejun consistent pentru o zi activa.',
             'ingredients': '2 felii paine integrala, 2 oua, 1/2 avocado, rosie, sare, piper',
             'instructions': 'Prajeste ouale. Intinde avocado pe paine. Adauga ouale si rosia.', 'calories': 420, 'day': 2, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=400&h=300&fit=crop'},
            {'title': 'Bowl cu orez, somon si edamame', 'description': 'Pranz inspirat din bucataria asiatica.',
             'ingredients': '80g orez, 120g somon, edamame, morcov ras, castravete, sos soia, susan',
             'instructions': 'Fierbe orezul. Grieleaza somonul. Aranjeaza totul in bol cu legumele si sosul.', 'calories': 520, 'day': 2, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1467003909585-2f8a72700288?w=400&h=300&fit=crop'},
            {'title': 'Piept de curcan cu cartofi dulci', 'description': 'Cina echilibrata bogata in proteine.',
             'ingredients': '150g piept curcan, 200g cartof dulce, brocoli, ulei masline, ierburi',
             'instructions': 'Coace cartofii dulci 25 min. Grieleaza curcanul. Gateste brocoli la aburi.', 'calories': 460, 'day': 2, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400&h=300&fit=crop'},
            {'title': 'Iaurt cu granola', 'description': 'Gustare crocanta si cremoasa.',
             'ingredients': '150g iaurt natural, 30g granola, miere',
             'instructions': 'Pune iaurtul in bol, adauga granola si un fir de miere.', 'calories': 200, 'day': 2, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1488477181946-6428a0291777?w=400&h=300&fit=crop'},

            # Miercuri
            {'title': 'Clatite proteice cu fructe', 'description': 'Mic dejun dulce si nutritiv.',
             'ingredients': '1 banana, 2 oua, 30g ovaz, fructe de padure, miere',
             'instructions': 'Mixeaza banana, ouale si ovazul. Prajeste clatitele. Serveste cu fructe.', 'calories': 360, 'day': 3, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1567620905732-2d1ec7ab7445?w=400&h=300&fit=crop'},
            {'title': 'Salata Caesar cu pui', 'description': 'Salata clasica cu dressing cremos.',
             'ingredients': '120g piept pui, salata romana, crutoane, parmezan, dressing Caesar',
             'instructions': 'Grieleaza puiul si taie-l felii. Amesteca salata cu dressingul. Adauga puiul si crutoane.', 'calories': 470, 'day': 3, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=400&h=300&fit=crop'},
            {'title': 'Risotto cu ciuperci', 'description': 'Cina italiana cremoasa si aromata.',
             'ingredients': '80g orez arborio, 150g ciuperci, ceapa, vin alb, parmezan, unt',
             'instructions': 'Caleste ceapa si ciupercile. Adauga orezul, vinul, apoi stocul treptat. Amesteca 18 min. Adauga parmezan.', 'calories': 480, 'day': 3, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1476124369491-e7addf5db371?w=400&h=300&fit=crop'},
            {'title': 'Fructe de sezon', 'description': 'Gustare naturala si hidratanta.',
             'ingredients': 'struguri, pere, kiwi',
             'instructions': 'Spala si taie fructele in portii.', 'calories': 140, 'day': 3, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1490474418585-ba9bad8fd0ea?w=400&h=300&fit=crop'},

            # Joi
            {'title': 'Ovaz cu mere caramelizate', 'description': 'Mic dejun cald si aromat.',
             'ingredients': '60g ovaz, 200ml lapte, 1 mar, scortisoara, unt, miere',
             'instructions': 'Fierbe ovazul cu laptele. Caleste marul cu unt si scortisoara. Serveste deasupra.', 'calories': 400, 'day': 4, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1517673400267-0251440c45dc?w=400&h=300&fit=crop'},
            {'title': 'Burger de pui cu salata coleslaw', 'description': 'Pranz gustos dar echilibrat.',
             'ingredients': '150g piept pui, 1 chifluta integrala, salata, rosie, coleslaw, mustar',
             'instructions': 'Formeaza burgerul din piept pui tocat. Grieleaza 5 min/parte. Asambleaza cu legumele.', 'calories': 520, 'day': 4, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400&h=300&fit=crop'},
            {'title': 'Supa de legume cu paine', 'description': 'Cina usoara si reconfortanta.',
             'ingredients': 'morcov, telina, cartof, ceapa, usturoi, patrunjel, paine integrala',
             'instructions': 'Fierbe legumele 20 min. Condimenteaza. Serveste cu paine calda.', 'calories': 350, 'day': 4, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1476718406336-bb5a9690ee2a?w=400&h=300&fit=crop'},
            {'title': 'Trail mix', 'description': 'Gustare energizanta cu nuci si fructe uscate.',
             'ingredients': '20g migdale, 15g stafide, 10g seminte floarea soarelui',
             'instructions': 'Amesteca toate ingredientele.', 'calories': 180, 'day': 4, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1473093295043-cdd812d0e601?w=400&h=300&fit=crop'},

            # Vineri
            {'title': 'Shakshuka', 'description': 'Mic dejun mediteranean cu oua in sos de rosii.',
             'ingredients': '2 oua, 200g rosii, ardei, ceapa, usturoi, chimion, patrunjel',
             'instructions': 'Caleste ceapa si ardeiul. Adauga rosiile si condimentele. Sparge ouale deasupra si acopera 5 min.', 'calories': 340, 'day': 5, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=400&h=300&fit=crop'},
            {'title': 'Pad thai cu pui', 'description': 'Pranz asiatic aromat si satios.',
             'ingredients': '80g noodles de orez, 120g pui, ou, germeni soia, arahide, lime, sos pad thai',
             'instructions': 'Fierbe noodles. Prajeste puiul. Adauga oul batut, sosul si noodles. Serveste cu arahide si lime.', 'calories': 530, 'day': 5, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1512058564366-18510be2db19?w=400&h=300&fit=crop'},
            {'title': 'Pizza integrala cu legume', 'description': 'Cina gustoasa de vineri.',
             'ingredients': 'aluat integral, sos rosii, mozzarella, ardei, ciuperci, masline, rucola',
             'instructions': 'Intinde aluatul. Adauga sosul, branza si legumele. Coace 12 min la 220°C. Adauga rucola.', 'calories': 520, 'day': 5, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=400&h=300&fit=crop'},
            {'title': 'Smoothie cu capsuni', 'description': 'Gustare racoritoare si vitaminizanta.',
             'ingredients': '150g capsuni, 100ml lapte, miere, gheata',
             'instructions': 'Mixeaza totul in blender.', 'calories': 140, 'day': 5, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1505252585461-04db1eb84625?w=400&h=300&fit=crop'},

            # Sambata
            {'title': 'French toast cu fructe', 'description': 'Mic dejun de weekend delicios.',
             'ingredients': '2 felii paine, 2 oua, lapte, vanilie, fructe de padure, sirop de artar',
             'instructions': 'Inmoaie painea in amestecul de oua si lapte. Prajeste. Serveste cu fructe si sirop.', 'calories': 420, 'day': 6, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1567620905732-2d1ec7ab7445?w=400&h=300&fit=crop'},
            {'title': 'Salata de paste cu pesto', 'description': 'Pranz usor de weekend.',
             'ingredients': '80g paste fusilli, pesto busuioc, rosii cherry, mozzarella mini, rucola',
             'instructions': 'Fierbe pastele. Amesteca cu pesto, rosii si mozzarella. Serveste cald sau rece.', 'calories': 490, 'day': 6, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1621996346565-e3dbc646d9a9?w=400&h=300&fit=crop'},
            {'title': 'Friptura de vita cu legume la cuptor', 'description': 'Cina festiva de weekend.',
             'ingredients': '150g muschi vita, cartofi, morcovi, ceapa, rozmarin, ulei masline',
             'instructions': 'Condimenteaza carnea. Taie legumele. Aseaza pe tava si coace 35 min la 200°C.', 'calories': 520, 'day': 6, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400&h=300&fit=crop'},
            {'title': 'Ciocolata neagra cu migdale', 'description': 'Gustare dulce cu antioxidanti.',
             'ingredients': '20g ciocolata neagra 70%, 15g migdale',
             'instructions': 'Savureaza ciocolata cu migdalele.', 'calories': 180, 'day': 6, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1497888329096-51c27beff665?w=400&h=300&fit=crop'},

            # Duminica
            {'title': 'Brunch cu oua Benedict', 'description': 'Mic dejun special de duminica.',
             'ingredients': '2 oua, 2 felii paine, sunca, sos hollandaise, spanac',
             'instructions': 'Poseaza ouale. Prajeste painea. Aseaza sunca, spanacul, ouale si sosul.', 'calories': 450, 'day': 7, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=400&h=300&fit=crop'},
            {'title': 'Tocana de pui cu legume', 'description': 'Pranz traditional cald si gustos.',
             'ingredients': '150g pulpa pui, ardei, rosii, ceapa, usturoi, boia, patrunjel',
             'instructions': 'Caleste ceapa si carnea. Adauga legumele si condimentele. Gateste 25 min.', 'calories': 440, 'day': 7, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400&h=300&fit=crop'},
            {'title': 'Salata calda de cartofi cu mustar', 'description': 'Cina usoara pentru finalul de saptamana.',
             'ingredients': '200g cartofi noi, ceapa verde, mustar Dijon, ulei masline, marar',
             'instructions': 'Fierbe cartofii. Amesteca cu dressingul de mustar si ceapa verde.', 'calories': 380, 'day': 7, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=400&h=300&fit=crop'},
            {'title': 'Popcorn de casa', 'description': 'Gustare usoara de duminica seara.',
             'ingredients': '40g porumb, ulei cocos, sare',
             'instructions': 'Incinge uleiul, adauga porumbul, acopera si asteapta sa se sparga.', 'calories': 160, 'day': 7, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1585937421612-70a008356fbe?w=400&h=300&fit=crop'},
        ]
        for r in d8_recipes:
            Recipe.objects.get_or_create(diet=d8, title=r['title'], day=r['day'], defaults=r)

        # === DIETA 9: Hipercaloric Clean Bulk (masa musculara) ===
        d9, _ = Diet.objects.get_or_create(
            name='Hipercaloric Clean Bulk',
            defaults={
                'goal': 'gain',
                'description': 'Plan alimentar curat, hipercaloric, cu accent pe proteine de calitate si carbohidrati complecsi. '
                               'Fara alimente procesate. Ideal pentru cresterea masei musculare curate.',
                'calories_per_day': 3200,
                'is_insulin_friendly': False,
            }
        )
        d9_recipes = [
            # Luni
            {'title': 'Ovaz cu whey si unt de arahide', 'description': 'Mic dejun hipercaloric si proteic.',
             'ingredients': '80g ovaz, 300ml lapte, 30g whey vanilie, 25g unt arahide, banana, miere',
             'instructions': 'Fierbe ovazul cu laptele. Adauga whey, untul de arahide, banana si miere.', 'calories': 680, 'day': 1, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1517673400267-0251440c45dc?w=400&h=300&fit=crop'},
            {'title': 'Piept de pui cu orez si broccoli', 'description': 'Pranz clasic bodybuilding.',
             'ingredients': '200g piept pui, 100g orez, 200g brocoli, ulei masline, usturoi',
             'instructions': 'Fierbe orezul. Grieleaza puiul condimentat. Gateste brocoli la aburi. Serveste cu ulei masline.', 'calories': 650, 'day': 1, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400&h=300&fit=crop'},
            {'title': 'Somon cu cartofi dulci si sparanghel', 'description': 'Cina bogata in omega-3 si carbohidrati complecsi.',
             'ingredients': '180g somon, 250g cartof dulce, sparanghel, lamaie, ulei masline',
             'instructions': 'Coace cartofii dulci 25 min. Grieleaza somonul 5 min/parte. Gateste sparanghelul la gratar.', 'calories': 720, 'day': 1, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1467003909585-2f8a72700288?w=400&h=300&fit=crop'},
            {'title': 'Shake proteic cu banana si ovaz', 'description': 'Gustare lichida hipercalorica.',
             'ingredients': '300ml lapte, 30g whey, 1 banana, 30g ovaz, 15g unt arahide',
             'instructions': 'Mixeaza totul in blender 40 secunde.', 'calories': 480, 'day': 1, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1505252585461-04db1eb84625?w=400&h=300&fit=crop'},

            # Marti
            {'title': 'Oua intregi cu paine si avocado', 'description': 'Mic dejun consistent cu grasimi sanatoase.',
             'ingredients': '4 oua, 2 felii paine integrala, 1 avocado, rosii cherry, sare, piper',
             'instructions': 'Prajeste ouale. Prajeste painea. Intinde avocado si adauga rosiile.', 'calories': 650, 'day': 2, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=400&h=300&fit=crop'},
            {'title': 'Paste cu carne tocata de vita', 'description': 'Pranz bogat in proteine si carbohidrati.',
             'ingredients': '100g paste, 180g carne vita tocata, sos rosii, ceapa, usturoi, parmezan',
             'instructions': 'Fierbe pastele. Prajeste carnea cu ceapa si usturoiul. Adauga sosul. Serveste cu parmezan.', 'calories': 720, 'day': 2, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1621996346565-e3dbc646d9a9?w=400&h=300&fit=crop'},
            {'title': 'Pui la cuptor cu cartofi', 'description': 'Cina consistenta cu proteine si carbohidrati.',
             'ingredients': '200g pulpa pui, 300g cartofi, ceapa, usturoi, rozmarin, ulei masline',
             'instructions': 'Condimenteaza puiul. Taie cartofii. Coace totul 40 min la 200°C.', 'calories': 680, 'day': 2, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400&h=300&fit=crop'},
            {'title': 'Branza de vaci cu miere si nuci', 'description': 'Gustare proteica si calorica.',
             'ingredients': '200g branza de vaci, 20g nuci, miere, scortisoara',
             'instructions': 'Amesteca branza cu miere. Adauga nucile si scortisoara.', 'calories': 380, 'day': 2, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1452195100486-9cc805987862?w=400&h=300&fit=crop'},

            # Miercuri
            {'title': 'Clatite proteice cu unt de arahide', 'description': 'Mic dejun dulce hipercaloric.',
             'ingredients': '2 oua, 1 banana, 30g whey, 30g ovaz, unt arahide, miere',
             'instructions': 'Mixeaza ouale, banana, whey si ovazul. Prajeste clatitele. Adauga unt arahide si miere.', 'calories': 620, 'day': 3, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1567620905732-2d1ec7ab7445?w=400&h=300&fit=crop'},
            {'title': 'Bowl cu vita, orez si legume', 'description': 'Pranz tip meal prep, bogat in nutrienti.',
             'ingredients': '180g vita slaba, 100g orez, brocoli, morcovi, sos soia, susan',
             'instructions': 'Fierbe orezul. Prajeste vita cu legumele si sosul. Aranjeaza in bol.', 'calories': 700, 'day': 3, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1512058564366-18510be2db19?w=400&h=300&fit=crop'},
            {'title': 'Curcan cu quinoa si spanac', 'description': 'Cina echilibrata cu proteine complete.',
             'ingredients': '200g piept curcan, 80g quinoa, spanac, rosii uscate, ulei masline',
             'instructions': 'Fierbe quinoa. Grieleaza curcanul. Caleste spanacul cu rosiile uscate.', 'calories': 640, 'day': 3, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400&h=300&fit=crop'},
            {'title': 'Iaurt grecesc cu granola si fructe', 'description': 'Gustare densa caloric.',
             'ingredients': '200g iaurt grecesc, 50g granola, fructe de padure, miere',
             'instructions': 'Combina iaurtul cu granola si fructele.', 'calories': 400, 'day': 3, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1488477181946-6428a0291777?w=400&h=300&fit=crop'},

            # Joi
            {'title': 'Sandwich proteic dublu', 'description': 'Mic dejun masiv cu proteine din oua si branza.',
             'ingredients': '3 oua, 2 felii paine integrala, sunca pui, cascaval, rosie, salata',
             'instructions': 'Prajeste ouale. Asambleaza sandwichul cu toate ingredientele.', 'calories': 580, 'day': 4, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=400&h=300&fit=crop'},
            {'title': 'Chili con carne cu orez', 'description': 'Pranz consistent, bogat in proteine si fibre.',
             'ingredients': '180g carne vita tocata, fasole rosie, rosii, ardei, ceapa, chimion, orez',
             'instructions': 'Prajeste carnea. Adauga legumele si condimentele. Gateste 20 min. Serveste cu orez.', 'calories': 750, 'day': 4, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400&h=300&fit=crop'},
            {'title': 'Pui teriyaki cu legume si noodles', 'description': 'Cina asiatica bogata in calorii.',
             'ingredients': '200g pui, noodles de orez, brocoli, ardei, morcov, sos teriyaki, susan',
             'instructions': 'Prajeste puiul cu legumele. Adauga sosul. Fierbe noodles si amesteca.', 'calories': 700, 'day': 4, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1512058564366-18510be2db19?w=400&h=300&fit=crop'},
            {'title': 'Toast cu avocado si seminte', 'description': 'Gustare cu grasimi sanatoase.',
             'ingredients': '2 felii paine, 1 avocado, seminte dovleac, fulgi chili, lamaie',
             'instructions': 'Prajeste painea. Intinde avocado, presara semintele si chili.', 'calories': 420, 'day': 4, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=400&h=300&fit=crop'},

            # Vineri
            {'title': 'Smoothie hipercaloric', 'description': 'Mic dejun lichid dens in nutrienti.',
             'ingredients': '300ml lapte, 30g whey, 1 banana, 30g ovaz, 25g unt arahide, cacao',
             'instructions': 'Mixeaza totul in blender. Bea imediat.', 'calories': 700, 'day': 5, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1505252585461-04db1eb84625?w=400&h=300&fit=crop'},
            {'title': 'Burrito cu pui si orez', 'description': 'Pranz mexican consistent.',
             'ingredients': '1 tortilla mare, 150g pui, orez, fasole neagra, porumb, smantana, salsa',
             'instructions': 'Grieleaza puiul. Umple tortilla cu orezul, puiul, fasolea si condimentele. Ruleaza.', 'calories': 750, 'day': 5, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1626700051175-6818013e1d4f?w=400&h=300&fit=crop'},
            {'title': 'Steak de vita cu cartofi si sparanghel', 'description': 'Cina premium hipercalorica.',
             'ingredients': '200g steak vita, 250g cartofi, sparanghel, unt, usturoi, rozmarin',
             'instructions': 'Scoate steakul la temperatura camerei. Prajeste 3 min/parte. Coace cartofii cu unt si usturoi.', 'calories': 780, 'day': 5, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400&h=300&fit=crop'},
            {'title': 'Mix energetic proteic', 'description': 'Gustare ideala post-antrenament.',
             'ingredients': '200g branza de vaci, 1 banana, 20g miere, 15g migdale',
             'instructions': 'Amesteca branza cu miere. Adauga banana si migdalele.', 'calories': 420, 'day': 5, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1452195100486-9cc805987862?w=400&h=300&fit=crop'},

            # Sambata
            {'title': 'Omleta gigant cu legume si cascaval', 'description': 'Mic dejun masiv de weekend.',
             'ingredients': '5 oua, ardei, ciuperci, ceapa, spanac, cascaval, paine',
             'instructions': 'Caleste legumele. Adauga ouale batute. Presara cascaval. Serveste cu paine.', 'calories': 650, 'day': 6, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=400&h=300&fit=crop'},
            {'title': 'Shawarma de pui cu garnitura', 'description': 'Pranz abundent inspirat oriental.',
             'ingredients': '200g pui, lipie, hummus, salata, rosii, castravete, sos usturoi, cartofi prajiti',
             'instructions': 'Condimenteaza si grieleaza puiul. Intinde hummus pe lipie. Adauga legumele si puiul.', 'calories': 800, 'day': 6, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400&h=300&fit=crop'},
            {'title': 'Lazanie cu carne de vita', 'description': 'Cina bogata, ideala pentru refacere musculara.',
             'ingredients': '200g carne vita, foi lasagna, sos bechamel, sos rosii, mozzarella, parmezan',
             'instructions': 'Pregateste sosul de carne si bechamelul. Stratifica foile cu sosurile si branza. Coace 35 min la 180°C.', 'calories': 750, 'day': 6, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1621996346565-e3dbc646d9a9?w=400&h=300&fit=crop'},
            {'title': 'Milkshake proteic cu ciocolata', 'description': 'Gustare desert hipercalorica.',
             'ingredients': '250ml lapte, 30g whey ciocolata, 1 banana, 20g unt arahide, gheata',
             'instructions': 'Mixeaza totul in blender.', 'calories': 480, 'day': 6, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1505252585461-04db1eb84625?w=400&h=300&fit=crop'},

            # Duminica
            {'title': 'Brunch proteic complet', 'description': 'Mic dejun masiv de refacere.',
             'ingredients': '4 oua, bacon pui, 2 felii paine, avocado, rosii, fasole alba in sos',
             'instructions': 'Prajeste ouale si baconul. Prajeste painea. Incalzeste fasolea. Asambleaza totul.', 'calories': 720, 'day': 7, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=400&h=300&fit=crop'},
            {'title': 'Pui cu paste si pesto', 'description': 'Pranz simplu dar caloric.',
             'ingredients': '180g piept pui, 100g paste penne, pesto busuioc, rosii cherry, parmezan',
             'instructions': 'Fierbe pastele. Grieleaza puiul. Amesteca cu pesto si rosii. Presara parmezan.', 'calories': 700, 'day': 7, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1621996346565-e3dbc646d9a9?w=400&h=300&fit=crop'},
            {'title': 'Tocana de curcan cu naut si orez', 'description': 'Cina traditionala bogata in proteine.',
             'ingredients': '200g curcan, naut, rosii, ceapa, usturoi, boia dulce, orez',
             'instructions': 'Caleste ceapa. Adauga curcanul si nautul. Adauga rosiile si condimentele. Gateste 25 min. Serveste cu orez.', 'calories': 680, 'day': 7, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400&h=300&fit=crop'},
            {'title': 'Tartine cu ricotta si miere', 'description': 'Gustare dulce de duminica.',
             'ingredients': '2 felii paine, 100g ricotta, miere, nuci, scortisoara',
             'instructions': 'Prajeste painea. Intinde ricotta. Adauga miere si nuci.', 'calories': 380, 'day': 7, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1452195100486-9cc805987862?w=400&h=300&fit=crop'},
        ]
        for r in d9_recipes:
            Recipe.objects.get_or_create(diet=d9, title=r['title'], day=r['day'], defaults=r)

        # === DIETA 10: Masa Musculara pentru Incepatori ===
        d10, _ = Diet.objects.get_or_create(
            name='Masa Musculara pentru Incepatori',
            defaults={
                'goal': 'gain',
                'description': 'Plan alimentar cu surplus caloric moderat, bazat pe alimente accesibile si retete simple. '
                               'Perfect pentru cei care abia incep sa construiasca masa musculara.',
                'calories_per_day': 2800,
                'is_insulin_friendly': False,
            }
        )
        d10_recipes = [
            # Luni
            {'title': 'Mic dejun clasic cu oua si paine', 'description': 'Simplu, rapid si eficient.',
             'ingredients': '4 oua, 2 felii paine alba, unt, rosie, cascaval felii',
             'instructions': 'Prajeste ouale in unt. Prajeste painea. Adauga cascavalul si rosia.', 'calories': 550, 'day': 1, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=400&h=300&fit=crop'},
            {'title': 'Piept de pui cu paste si sos', 'description': 'Pranzul perfect pentru crestere musculara.',
             'ingredients': '180g piept pui, 100g paste, sos rosii, ceapa, usturoi, ulei masline',
             'instructions': 'Fierbe pastele. Caleste ceapa si usturoiul. Prajeste puiul. Amesteca totul cu sosul.', 'calories': 620, 'day': 1, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1621996346565-e3dbc646d9a9?w=400&h=300&fit=crop'},
            {'title': 'Orez cu carne tocata si legume', 'description': 'Cina simpla si calorica.',
             'ingredients': '150g carne tocata mixta, 80g orez, ardei, ceapa, rosii, boia',
             'instructions': 'Fierbe orezul. Prajeste carnea cu legumele. Amesteca si condimenteaza.', 'calories': 580, 'day': 1, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400&h=300&fit=crop'},
            {'title': 'Sandvis cu ton si ou', 'description': 'Gustare consistenta post-antrenament.',
             'ingredients': '100g ton conserva, 1 ou fiert, 2 felii paine, maioneza, salata',
             'instructions': 'Amesteca tonul cu oul tocat si maioneza. Pune pe paine cu salata.', 'calories': 420, 'day': 1, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=400&h=300&fit=crop'},

            # Marti
            {'title': 'Cereale cu lapte si banana', 'description': 'Mic dejun rapid si energizant.',
             'ingredients': '60g cereale integrale, 250ml lapte, 1 banana, miere',
             'instructions': 'Pune cerealele in bol. Adauga laptele, banana taiata si miere.', 'calories': 480, 'day': 2, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1517673400267-0251440c45dc?w=400&h=300&fit=crop'},
            {'title': 'Kebab de pui cu pita si salata', 'description': 'Pranz gustos si bogat in proteine.',
             'ingredients': '180g pui, 1 pita, salata, rosii, ceapa, iaurt, usturoi',
             'instructions': 'Condimenteaza si grieleaza puiul. Incalzeste pita. Adauga legumele si sosul de iaurt.', 'calories': 600, 'day': 2, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400&h=300&fit=crop'},
            {'title': 'Cartofi la cuptor cu branza si bacon', 'description': 'Cina calorica si satisfacatoare.',
             'ingredients': '300g cartofi, 50g cascaval, bacon, smantana, ceapa verde',
             'instructions': 'Coace cartofii 40 min. Taie deasupra, adauga smantana, baconul si branza. Coace inca 10 min.', 'calories': 620, 'day': 2, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400&h=300&fit=crop'},
            {'title': 'Lapte cu cacao si biscuiti', 'description': 'Gustare accesibila si placuta.',
             'ingredients': '300ml lapte, 20g cacao, miere, 3 biscuiti integrali',
             'instructions': 'Incalzeste laptele cu cacao si miere. Serveste cu biscuitii.', 'calories': 350, 'day': 2, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1497888329096-51c27beff665?w=400&h=300&fit=crop'},

            # Miercuri
            {'title': 'Toast-uri cu ou si sunca', 'description': 'Mic dejun consistent si rapid.',
             'ingredients': '3 oua, 3 felii paine, sunca pui, cascaval, unt',
             'instructions': 'Prajeste ouale. Prajeste painea in unt. Adauga sunca si cascavalul.', 'calories': 560, 'day': 3, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=400&h=300&fit=crop'},
            {'title': 'Spaghete bolognese', 'description': 'Pranz clasic, bogat in calorii si proteine.',
             'ingredients': '100g spaghete, 150g carne vita tocata, sos rosii, ceapa, morcov, telina, parmezan',
             'instructions': 'Fierbe pastele. Caleste legumele. Adauga carnea si sosul. Gateste 15 min. Amesteca cu pastele.', 'calories': 680, 'day': 3, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1621996346565-e3dbc646d9a9?w=400&h=300&fit=crop'},
            {'title': 'Pui la tigaie cu orez si mazare', 'description': 'Cina echilibrata si simpla.',
             'ingredients': '180g pui, 80g orez, mazare, morcov, sos soia, ulei',
             'instructions': 'Fierbe orezul. Prajeste puiul taiat cubulete. Adauga legumele si sosul. Serveste cu orezul.', 'calories': 600, 'day': 3, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1512058564366-18510be2db19?w=400&h=300&fit=crop'},
            {'title': 'Branza de vaci cu fructe', 'description': 'Gustare proteica dulce.',
             'ingredients': '200g branza de vaci, 1 banana, miere, scortisoara',
             'instructions': 'Amesteca branza cu banana taiata, miere si scortisoara.', 'calories': 320, 'day': 3, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1452195100486-9cc805987862?w=400&h=300&fit=crop'},

            # Joi
            {'title': 'Iaurt cu musli si fructe', 'description': 'Mic dejun rapid si nutritiv.',
             'ingredients': '250g iaurt, 50g musli, banana, capsuni, miere',
             'instructions': 'Pune iaurtul in bol. Adauga musli, fructele si miere.', 'calories': 450, 'day': 4, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1488477181946-6428a0291777?w=400&h=300&fit=crop'},
            {'title': 'Cotlet de porc cu piure', 'description': 'Pranz traditional romanesc.',
             'ingredients': '180g cotlet porc, 250g cartofi, lapte, unt, salata verde, rosie',
             'instructions': 'Prajeste cotletul. Fierbe cartofii si fa piure cu lapte si unt. Serveste cu salata.', 'calories': 700, 'day': 4, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400&h=300&fit=crop'},
            {'title': 'Ciorba de pui cu taitei', 'description': 'Cina calda si reconfortanta.',
             'ingredients': '150g pui, taitei, morcov, ceapa, telina, patrunjel, lamaie',
             'instructions': 'Fierbe puiul cu legumele 20 min. Adauga taiteii si fierbe inca 5 min. Adauga patrunjel si lamaie.', 'calories': 450, 'day': 4, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1476718406336-bb5a9690ee2a?w=400&h=300&fit=crop'},
            {'title': 'Covrigei cu branza', 'description': 'Gustare salata si proteica.',
             'ingredients': '50g covrigei, 50g branza topita',
             'instructions': 'Serveste covrigeii cu branza.', 'calories': 280, 'day': 4, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1585937421612-70a008356fbe?w=400&h=300&fit=crop'},

            # Vineri
            {'title': 'Omleta mare cu cascaval si sunca', 'description': 'Mic dejun bogat in proteine.',
             'ingredients': '4 oua, cascaval, sunca, ardei, ceapa, paine',
             'instructions': 'Bate ouale. Adauga ingredientele taiate. Gateste la foc mediu. Serveste cu paine.', 'calories': 580, 'day': 5, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=400&h=300&fit=crop'},
            {'title': 'Gyros de pui cu cartofi', 'description': 'Pranz tip fast-food sanatos.',
             'ingredients': '200g pui, lipie, cartofi prajiti, salata, rosii, sos tzatziki',
             'instructions': 'Condimenteaza si prajeste puiul. Prajeste cartofii. Asambleaza in lipie cu legumele si sosul.', 'calories': 750, 'day': 5, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400&h=300&fit=crop'},
            {'title': 'Macaroane cu branza la cuptor', 'description': 'Cina clasica confort food.',
             'ingredients': '120g macaroane, 100g cascaval, 50g smantana, lapte, unt, pesmet',
             'instructions': 'Fierbe macaroanele. Fa sosul de branza cu lapte si smantana. Amesteca, presara pesmet si coace 15 min.', 'calories': 620, 'day': 5, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1621996346565-e3dbc646d9a9?w=400&h=300&fit=crop'},
            {'title': 'Shake simplu cu lapte si banana', 'description': 'Gustare rapida si calorica.',
             'ingredients': '300ml lapte, 1 banana mare, miere, unt arahide',
             'instructions': 'Mixeaza totul in blender.', 'calories': 400, 'day': 5, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1505252585461-04db1eb84625?w=400&h=300&fit=crop'},

            # Sambata
            {'title': 'Oua cu bacon si cartofi prajiti', 'description': 'Brunch de weekend satios.',
             'ingredients': '4 oua, bacon pui, 200g cartofi, ceapa, ardei, ulei',
             'instructions': 'Prajeste cartofii cu ceapa. Adauga baconul si ouale. Gateste pana sunt gata.', 'calories': 650, 'day': 6, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=400&h=300&fit=crop'},
            {'title': 'Shaorma de casa cu de toate', 'description': 'Pranz popular, varianta de casa.',
             'ingredients': '200g pui, lipie, salata, rosii, castravete, varza, ceapa, mustar, ketchup, maioneza',
             'instructions': 'Grieleaza puiul condimentat. Taie legumele. Asambleaza in lipie cu sosurile preferate.', 'calories': 720, 'day': 6, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400&h=300&fit=crop'},
            {'title': 'Pizza de casa cu sunca si ciuperci', 'description': 'Cina gustoasa de sambata.',
             'ingredients': 'aluat pizza, sos rosii, mozzarella, sunca, ciuperci, ardei, masline',
             'instructions': 'Intinde aluatul. Adauga sosul, branza si toppingurile. Coace 12 min la 220°C.', 'calories': 680, 'day': 6, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=400&h=300&fit=crop'},
            {'title': 'Corn cu ciocolata si lapte', 'description': 'Gustare dulce de weekend.',
             'ingredients': '1 corn cu ciocolata, 250ml lapte',
             'instructions': 'Savureaza cornul cu un pahar de lapte.', 'calories': 380, 'day': 6, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1497888329096-51c27beff665?w=400&h=300&fit=crop'},

            # Duminica
            {'title': 'Clatite cu gem si smantana', 'description': 'Mic dejun dulce traditional.',
             'ingredients': '2 oua, 150ml lapte, 80g faina, gem, smantana, zahar pudra',
             'instructions': 'Amesteca ouale, laptele si faina. Prajeste clatitele subtiri. Pune gem si smantana.', 'calories': 520, 'day': 7, 'meal_type': 'breakfast', 'image_url': 'https://images.unsplash.com/photo-1567620905732-2d1ec7ab7445?w=400&h=300&fit=crop'},
            {'title': 'Friptura de porc cu piure si salata', 'description': 'Pranz traditional de duminica.',
             'ingredients': '200g friptura porc, 250g cartofi, lapte, unt, salata, rosii, castravete',
             'instructions': 'Coace friptura 45 min la 180°C. Fierbe cartofii si fa piure. Pregateste salata.', 'calories': 750, 'day': 7, 'meal_type': 'lunch', 'image_url': 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400&h=300&fit=crop'},
            {'title': 'Supa crema de cartofi cu crutoane', 'description': 'Cina usoara dar satioasa.',
             'ingredients': '300g cartofi, ceapa, usturoi, smantana, crutoane, chives',
             'instructions': 'Fierbe cartofii cu ceapa. Mixeaza. Adauga smantana. Serveste cu crutoane.', 'calories': 420, 'day': 7, 'meal_type': 'dinner', 'image_url': 'https://images.unsplash.com/photo-1476718406336-bb5a9690ee2a?w=400&h=300&fit=crop'},
            {'title': 'Fructe cu iaurt si miere', 'description': 'Gustare usoara de duminica seara.',
             'ingredients': '150g iaurt, fructe de sezon, miere',
             'instructions': 'Pune iaurtul in bol cu fructele si miere.', 'calories': 200, 'day': 7, 'meal_type': 'snack', 'image_url': 'https://images.unsplash.com/photo-1488477181946-6428a0291777?w=400&h=300&fit=crop'},
        ]
        for r in d10_recipes:
            Recipe.objects.get_or_create(diet=d10, title=r['title'], day=r['day'], defaults=r)

        self.stdout.write(self.style.SUCCESS(f'Diete: {Diet.objects.count()}, Retete: {Recipe.objects.count()}'))

    def _seed_workouts(self):
        self.stdout.write('--- Antrenamente ---')
        workouts_data = [
            # === SLABIRE ===
            {'title': 'HIIT 20 Minute - Acasa', 'short_description': 'Antrenament intens pentru arderea grasimilor, fara echipament. 40s lucru, 20s pauza.',
             'environment': 'home', 'difficulty': 'medium', 'duration_minutes': 20, 'goal': 'lose',
             'youtube_url': 'https://www.youtube.com/watch?v=ml6cT4AZdqI',
             'image_url': 'https://images.unsplash.com/photo-1534258936925-c58bed479fcb?w=400&h=300&fit=crop'},
            {'title': 'Full Body cu Greutate Proprie', 'short_description': 'Antrenament complet de rezistenta si tonifiere. 3 seturi, 15 repetari per exercitiu.',
             'environment': 'home', 'difficulty': 'easy', 'duration_minutes': 30, 'goal': 'lose',
             'youtube_url': 'https://www.youtube.com/watch?v=UItWltVZZmE',
             'image_url': 'https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=400&h=300&fit=crop'},
            {'title': 'Circuit Cardio in Parc', 'short_description': 'Jogging combinat cu exercitii de forta la banca. Ideal dimineata.',
             'environment': 'outdoor', 'difficulty': 'medium', 'duration_minutes': 40, 'goal': 'lose',
             'youtube_url': 'https://www.youtube.com/watch?v=CBWQGb4LyAM',
             'image_url': 'https://images.unsplash.com/photo-1571008887538-b36bb32f4571?w=400&h=300&fit=crop'},
            {'title': 'Circuit Ardere la Sala', 'short_description': 'Antrenament circular cu aparate: 8 exercitii, 3 runde, pauza minima.',
             'environment': 'gym', 'difficulty': 'hard', 'duration_minutes': 45, 'goal': 'lose',
             'youtube_url': 'https://www.youtube.com/watch?v=tBzbv4KcJRU',
             'image_url': 'https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=400&h=300&fit=crop'},
            {'title': 'Saritura la Coarda', 'short_description': 'Cardio intens cu coarda de sarit. 30s sprint, 15s pauza x 20 runde. Ardere maxima.',
             'environment': 'home', 'difficulty': 'medium', 'duration_minutes': 15, 'goal': 'lose',
             'youtube_url': 'https://www.youtube.com/watch?v=a0Hrvh4RS3o',
             'image_url': 'https://images.unsplash.com/photo-1534258936925-c58bed479fcb?w=400&h=300&fit=crop'},
            {'title': 'Kickboxing Acasa', 'short_description': 'Combinatii de lovituri si miscare. Arzi calorii si elibereaza stresul.',
             'environment': 'home', 'difficulty': 'hard', 'duration_minutes': 35, 'goal': 'lose',
             'youtube_url': 'https://www.youtube.com/watch?v=0FNPcDNuSAI',
             'image_url': 'https://images.unsplash.com/photo-1517438322307-e67111335449?w=400&h=300&fit=crop'},
            {'title': 'Mers Rapid in Natura', 'short_description': 'Power walking 45 minute pe teren variat. Accesibil si eficient pt incepatori.',
             'environment': 'outdoor', 'difficulty': 'easy', 'duration_minutes': 45, 'goal': 'lose',
             'youtube_url': 'https://www.youtube.com/watch?v=njeZ29umqVE',
             'image_url': 'https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?w=400&h=300&fit=crop'},

            # === MENTINERE ===
            {'title': 'Antrenament Picioare si Umeri', 'short_description': 'Hipertrofie clasica cu accent pe Squat si Military Press. 4 seturi, 10-12 rep.',
             'environment': 'gym', 'difficulty': 'medium', 'duration_minutes': 50, 'goal': 'maintain',
             'youtube_url': 'https://www.youtube.com/watch?v=EotSw18oR9w',
             'image_url': 'https://images.unsplash.com/photo-1574680178050-55c6a6a96e0a?w=400&h=300&fit=crop'},
            {'title': 'Yoga Flow 30 Minute', 'short_description': 'Sesiune de yoga pentru flexibilitate, echilibru si relaxare.',
             'environment': 'home', 'difficulty': 'easy', 'duration_minutes': 30, 'goal': 'maintain',
             'youtube_url': 'https://www.youtube.com/watch?v=v7AYKMP6rOE',
             'image_url': 'https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=400&h=300&fit=crop'},
            {'title': 'Alergare Moderata Outdoor', 'short_description': 'Jogging constant 30-40 minute la puls moderat. Bun pentru rezistenta.',
             'environment': 'outdoor', 'difficulty': 'easy', 'duration_minutes': 35, 'goal': 'maintain',
             'youtube_url': 'https://www.youtube.com/watch?v=w0Ssrmjgkf0',
             'image_url': 'https://images.unsplash.com/photo-1571008887538-b36bb32f4571?w=400&h=300&fit=crop'},
            {'title': 'Pilates Acasa', 'short_description': 'Exercitii de core si flexibilitate. Tonifica fara impact. Ideal dimineata sau seara.',
             'environment': 'home', 'difficulty': 'easy', 'duration_minutes': 40, 'goal': 'maintain',
             'youtube_url': 'https://www.youtube.com/watch?v=K56Z12XNQ5c',
             'image_url': 'https://images.unsplash.com/photo-1518611012118-696072aa579a?w=400&h=300&fit=crop'},
            {'title': 'Ciclism Outdoor', 'short_description': 'Pedalat moderat 1 ora pe traseu plat sau usor variat. Bun pentru rezistenta si picioare.',
             'environment': 'outdoor', 'difficulty': 'medium', 'duration_minutes': 60, 'goal': 'maintain',
             'youtube_url': 'https://www.youtube.com/watch?v=ZiGE3-L4vyg',
             'image_url': 'https://images.unsplash.com/photo-1517649763962-0c623066013b?w=400&h=300&fit=crop'},
            {'title': 'Stretching si Mobilitate', 'short_description': 'Rutina completa de stretching pt tot corpul. Previne accidentari si reduce tensiunea.',
             'environment': 'home', 'difficulty': 'easy', 'duration_minutes': 25, 'goal': 'maintain',
             'youtube_url': 'https://www.youtube.com/watch?v=L_xrDAtykMI',
             'image_url': 'https://images.unsplash.com/photo-1518611012118-696072aa579a?w=400&h=300&fit=crop'},
            {'title': 'Inot - Rezistenta Cardio', 'short_description': 'Sesiune de inot liber 30 min. Lucreaza tot corpul fara impact pe articulatii.',
             'environment': 'gym', 'difficulty': 'medium', 'duration_minutes': 40, 'goal': 'maintain',
             'youtube_url': 'https://www.youtube.com/watch?v=ZNzsscbiylk',
             'image_url': 'https://images.unsplash.com/photo-1519315901367-f34ff9154487?w=400&h=300&fit=crop'},
            {'title': 'Abdomen si Core 15 Minute', 'short_description': 'Circuit rapid de abdomen: plank, crunches, russian twist, leg raises. 3 runde.',
             'environment': 'home', 'difficulty': 'medium', 'duration_minutes': 15, 'goal': 'maintain',
             'youtube_url': 'https://www.youtube.com/watch?v=5hgJsPk6fa0',
             'image_url': 'https://images.unsplash.com/photo-1571019614242-c5c5dee9f50b?w=400&h=300&fit=crop'},

            # === MASA MUSCULARA ===
            {'title': 'Push Pull Legs - Piept si Spate', 'short_description': 'Bench Press, Ramat cu Bara, Tractiuni, Flotari. 4 seturi, 8-10 rep.',
             'environment': 'gym', 'difficulty': 'hard', 'duration_minutes': 60, 'goal': 'gain',
             'youtube_url': 'https://www.youtube.com/watch?v=qVek72z3F1U',
             'image_url': 'https://images.unsplash.com/photo-1581009146145-b5ef050c2e1e?w=400&h=300&fit=crop'},
            {'title': 'Picioare - Volum Maxim', 'short_description': 'Squat, Deadlift, Presa picioare. 5 seturi grele, 6-8 repetari.',
             'environment': 'gym', 'difficulty': 'hard', 'duration_minutes': 55, 'goal': 'gain',
             'youtube_url': 'https://www.youtube.com/watch?v=ocUNowzxgb0',
             'image_url': 'https://images.unsplash.com/photo-1574680178050-55c6a6a96e0a?w=400&h=300&fit=crop'},
            {'title': 'Brate si Umeri Detaliat', 'short_description': 'Biceps, Triceps, Umeri - exercitii de izolare. 4 seturi, 12 repetari.',
             'environment': 'gym', 'difficulty': 'medium', 'duration_minutes': 45, 'goal': 'gain',
             'youtube_url': 'https://www.youtube.com/watch?v=Ua6phRsVMFo',
             'image_url': 'https://images.unsplash.com/photo-1581009146145-b5ef050c2e1e?w=400&h=300&fit=crop'},
            {'title': 'Deadlift si Spate - Forta', 'short_description': 'Deadlift conventional, ramat, pullover, shrugs. 5 seturi, 5-8 rep pt forta pura.',
             'environment': 'gym', 'difficulty': 'hard', 'duration_minutes': 50, 'goal': 'gain',
             'youtube_url': 'https://www.youtube.com/watch?v=r4MzxtBKyNE',
             'image_url': 'https://images.unsplash.com/photo-1526401485004-46910ecc8e51?w=400&h=300&fit=crop'},
            {'title': 'Tractiuni si Flotari - Calisthenics', 'short_description': 'Antrenament cu greutatea corpului: pull-ups, push-ups, dips, L-sit. Progresie lenta.',
             'environment': 'outdoor', 'difficulty': 'hard', 'duration_minutes': 45, 'goal': 'gain',
             'youtube_url': 'https://www.youtube.com/watch?v=6zUjKIGn0Vs',
             'image_url': 'https://images.unsplash.com/photo-1598971639058-fab3c3109a00?w=400&h=300&fit=crop'},
            {'title': 'Kettlebell Total Body', 'short_description': 'Swing, Clean & Press, Goblet Squat, Turkish Get-up. 4 seturi, 10 rep fiecare.',
             'environment': 'home', 'difficulty': 'medium', 'duration_minutes': 35, 'goal': 'gain',
             'youtube_url': 'https://www.youtube.com/watch?v=VCcar3MA07w',
             'image_url': 'https://images.unsplash.com/photo-1517963628607-235ccdd5476c?w=400&h=300&fit=crop'},
            {'title': 'Antrenament Functional Outdoor', 'short_description': 'Exercitii cu greutatea corpului in parc: burpees, box jumps, sprints, bear crawl.',
             'environment': 'outdoor', 'difficulty': 'medium', 'duration_minutes': 40, 'goal': 'gain',
             'youtube_url': 'https://www.youtube.com/watch?v=IODxDxX7oi4',
             'image_url': 'https://images.unsplash.com/photo-1541534741688-6078c6bfb5c5?w=400&h=300&fit=crop'},
        ]
        for w in workouts_data:
            Workout.objects.get_or_create(title=w['title'], defaults=w)
        self.stdout.write(self.style.SUCCESS(f'Antrenamente: {Workout.objects.count()}'))

    def _seed_citate(self):
        self.stdout.write('--- Citate ---')
        Citat.objects.all().delete()
        citate = [
            {'tip': 'slabit', 'text': 'Motivatia te face sa incepi, obiceiul te face sa continui. Nu renunta la Ziua 2!'},
            {'tip': 'mentinere', 'text': 'Echilibrul nu inseamna sa faci o singura data perfect, ci sa te ridici de fiecare data cand cazi.'},
            {'tip': 'ingrasare', 'text': 'Progresul nu este liniar. Fii consistent, iar muschii vor creste.'},
        ]
        for c in citate:
            Citat.objects.create(**c)
        self.stdout.write(self.style.SUCCESS(f'Citate: {Citat.objects.count()}'))

    def _seed_retete_index(self):
        self.stdout.write('--- Retete pt pagina landing ---')
        Reteta.objects.all().delete()
        # 3 diete x 7 zile x 5 mese = 105 retete
        retete = [
            # ========== SLABIT (Deficit Caloric) ~1500 kcal/zi ==========
            # Ziua 1
            {'nume': 'Omleta cu Spanac si Rosii', 'tip': 'slabit', 'masa': 'mic_dejun', 'zi': 1, 'kcal': 320, 'proteine': 24, 'carbohidrati': 8, 'grasimi': 22,
             'img_url': 'https://images.unsplash.com/photo-1510693206972-df098062cb71?w=400&h=300&fit=crop',
             'instructiuni': 'Bate 3 oua cu sare si piper. Caleste spanacul si rosiile cherry taiate in tigaia cu putin ulei de masline. Toarna ouale si gateste la foc mic 3-4 minute. Impatureste si serveste.'},
            {'nume': 'Mar Verde cu Unt de Migdale', 'tip': 'slabit', 'masa': 'gustare_1', 'zi': 1, 'kcal': 180, 'proteine': 5, 'carbohidrati': 22, 'grasimi': 9,
             'img_url': 'https://images.unsplash.com/photo-1568702846914-96b305d2uj38?w=400&h=300&fit=crop',
             'instructiuni': 'Taie marul in felii subtiri. Serveste cu o lingurita de unt de migdale natural, fara zahar adaugat.'},
            {'nume': 'Piept de Pui la Gratar cu Salata', 'tip': 'slabit', 'masa': 'pranz', 'zi': 1, 'kcal': 420, 'proteine': 38, 'carbohidrati': 12, 'grasimi': 18,
             'img_url': 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=400&h=300&fit=crop',
             'instructiuni': 'Condimenteaza pieptul de pui cu boia, usturoi praf si oregano. Gateste la gratar 6-7 min pe fiecare parte. Serveste pe un pat de salata verde, rosii, castraveti si dressing de lamaie.'},
            {'nume': 'Iaurt Grecesc cu Seminte', 'tip': 'slabit', 'masa': 'gustare_2', 'zi': 1, 'kcal': 150, 'proteine': 12, 'carbohidrati': 10, 'grasimi': 7,
             'img_url': 'https://images.unsplash.com/photo-1488477181946-6428a0291777?w=400&h=300&fit=crop',
             'instructiuni': 'Pune 150g iaurt grecesc 2% intr-un bol. Presara seminte de chia si seminte de in. Adauga cateva fructe de padure.'},
            {'nume': 'Supa Crema de Broccoli', 'tip': 'slabit', 'masa': 'cina', 'zi': 1, 'kcal': 280, 'proteine': 14, 'carbohidrati': 20, 'grasimi': 12,
             'img_url': 'https://images.unsplash.com/photo-1547592166-23ac45744acd?w=400&h=300&fit=crop',
             'instructiuni': 'Fierbe broccoli si o ceapa in supa de legume 15 min. Mixeaza cu blenderul vertical pana devine cremos. Adauga sare, piper si o lingura de smantana light.'},
            # Ziua 2
            {'nume': 'Smoothie Verde Proteic', 'tip': 'slabit', 'masa': 'mic_dejun', 'zi': 2, 'kcal': 290, 'proteine': 25, 'carbohidrati': 30, 'grasimi': 8,
             'img_url': 'https://images.unsplash.com/photo-1638176066666-ffb2f013c7dd?w=400&h=300&fit=crop',
             'instructiuni': 'Mixeaza 1 banana, o mana de spanac, 1 scoop proteina whey vanilie, 200ml lapte de migdale si cateva cuburi de gheata. Mixeaza 60 secunde.'},
            {'nume': 'Morcovi Baby cu Hummus', 'tip': 'slabit', 'masa': 'gustare_1', 'zi': 2, 'kcal': 160, 'proteine': 6, 'carbohidrati': 18, 'grasimi': 8,
             'img_url': 'https://images.unsplash.com/photo-1613478881427-d31e0f514623?w=400&h=300&fit=crop',
             'instructiuni': 'Spala morcovii baby si serveste-i cu 3 linguri de hummus clasic. Poti adauga si bete de telina.'},
            {'nume': 'Quinoa cu Ton si Avocado', 'tip': 'slabit', 'masa': 'pranz', 'zi': 2, 'kcal': 450, 'proteine': 32, 'carbohidrati': 35, 'grasimi': 18,
             'img_url': 'https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=400&h=300&fit=crop',
             'instructiuni': 'Fierbe quinoa conform instructiunilor. Amesteca cu ton scurs, avocado feliat, rosii cherry si suc de lamaie. Condimenteaza cu sare si piper.'},
            {'nume': 'Batoane Proteice Homemade', 'tip': 'slabit', 'masa': 'gustare_2', 'zi': 2, 'kcal': 140, 'proteine': 14, 'carbohidrati': 12, 'grasimi': 5,
             'img_url': 'https://images.unsplash.com/photo-1622484212850-eb596d769edc?w=400&h=300&fit=crop',
             'instructiuni': 'Amesteca proteina whey cu unt de arahide si fulgi de ovaz. Formeaza batoane si pune la frigider 1 ora.'},
            {'nume': 'Somon la Cuptor cu Sparanghel', 'tip': 'slabit', 'masa': 'cina', 'zi': 2, 'kcal': 380, 'proteine': 35, 'carbohidrati': 8, 'grasimi': 22,
             'img_url': 'https://images.unsplash.com/photo-1467003909585-2f8a72700288?w=400&h=300&fit=crop',
             'instructiuni': 'Aseaza fileul de somon si sparanghelul pe tava cu hartie de copt. Unge cu ulei de masline, sare, piper si lamaie. Coace 18 min la 200°C.'},
            # Ziua 3
            {'nume': 'Iaurt cu Granola si Fructe', 'tip': 'slabit', 'masa': 'mic_dejun', 'zi': 3, 'kcal': 310, 'proteine': 18, 'carbohidrati': 35, 'grasimi': 10,
             'img_url': 'https://images.unsplash.com/photo-1495214783159-3503fd1b572d?w=400&h=300&fit=crop',
             'instructiuni': 'Pune iaurt grecesc intr-un bol, adauga 30g granola low-sugar si fructe de padure proaspete (afine, zmeura, capsuni).'},
            {'nume': 'Castravete cu Branza Cottage', 'tip': 'slabit', 'masa': 'gustare_1', 'zi': 3, 'kcal': 120, 'proteine': 14, 'carbohidrati': 5, 'grasimi': 5,
             'img_url': 'https://images.unsplash.com/photo-1550304943-4f24f54ddde9?w=400&h=300&fit=crop',
             'instructiuni': 'Taie castravetele in rondele. Serveste cu 100g branza cottage si putina sare si marar.'},
            {'nume': 'Wrap cu Curcan si Legume', 'tip': 'slabit', 'masa': 'pranz', 'zi': 3, 'kcal': 400, 'proteine': 30, 'carbohidrati': 32, 'grasimi': 14,
             'img_url': 'https://images.unsplash.com/photo-1626700051175-6818013e1d4f?w=400&h=300&fit=crop',
             'instructiuni': 'Incalzeste tortilla integrala. Pune piept de curcan feliat, salata, rosii, castraveti si o lingura de mustar. Ruleaza strans.'},
            {'nume': 'Migdale Crude (15 buc)', 'tip': 'slabit', 'masa': 'gustare_2', 'zi': 3, 'kcal': 140, 'proteine': 5, 'carbohidrati': 5, 'grasimi': 12,
             'img_url': 'https://images.unsplash.com/photo-1508061253366-f7da158b6d46?w=400&h=300&fit=crop',
             'instructiuni': 'Portie de 15 migdale crude, neprajite. Se pot combina cu cateva stafide pentru un mix energizant.'},
            {'nume': 'Linte Rosie cu Curry', 'tip': 'slabit', 'masa': 'cina', 'zi': 3, 'kcal': 350, 'proteine': 20, 'carbohidrati': 40, 'grasimi': 8,
             'img_url': 'https://images.unsplash.com/photo-1585937421612-70a008356fbe?w=400&h=300&fit=crop',
             'instructiuni': 'Caleste ceapa si usturoiul. Adauga linte rosie spalata, pasta de curry, lapte de cocos light si supa de legume. Fierbe 20 min la foc mic.'},
            # Ziua 4
            {'nume': 'Oua Posate pe Toast Integral', 'tip': 'slabit', 'masa': 'mic_dejun', 'zi': 4, 'kcal': 300, 'proteine': 20, 'carbohidrati': 25, 'grasimi': 14,
             'img_url': 'https://images.unsplash.com/photo-1525351484163-7529414344d8?w=400&h=300&fit=crop',
             'instructiuni': 'Fierbe apa cu putin otet. Sparge ouale si lasa-le sa fiarba 3 minute. Prajeste painea integrala si asaza ouale deasupra. Presara sare si piper.'},
            {'nume': 'Banana cu Unt de Arahide', 'tip': 'slabit', 'masa': 'gustare_1', 'zi': 4, 'kcal': 190, 'proteine': 6, 'carbohidrati': 26, 'grasimi': 9,
             'img_url': 'https://images.unsplash.com/photo-1571771894821-ce9b6c11b08e?w=400&h=300&fit=crop',
             'instructiuni': 'Taie banana pe jumatate pe lungime. Intinde o lingurita de unt de arahide natural pe fiecare jumatate.'},
            {'nume': 'Salata de Naut cu Legume', 'tip': 'slabit', 'masa': 'pranz', 'zi': 4, 'kcal': 380, 'proteine': 18, 'carbohidrati': 42, 'grasimi': 14,
             'img_url': 'https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=400&h=300&fit=crop',
             'instructiuni': 'Amesteca naut fiert cu rosii cuburi, castravete, ceapa rosie, patrunjel. Dressing: ulei de masline, lamaie, sare, chimion.'},
            {'nume': 'Telina cu Unt de Migdale', 'tip': 'slabit', 'masa': 'gustare_2', 'zi': 4, 'kcal': 110, 'proteine': 3, 'carbohidrati': 5, 'grasimi': 9,
             'img_url': 'https://images.unsplash.com/photo-1473093295043-cdd812d0e601?w=400&h=300&fit=crop',
             'instructiuni': 'Taie tulpini de telina in bete de 10cm. Serveste cu o lingurita de unt de migdale.'},
            {'nume': 'Cod cu Legume la Cuptor', 'tip': 'slabit', 'masa': 'cina', 'zi': 4, 'kcal': 320, 'proteine': 32, 'carbohidrati': 15, 'grasimi': 12,
             'img_url': 'https://images.unsplash.com/photo-1519708227418-c8fd9a32b7a2?w=400&h=300&fit=crop',
             'instructiuni': 'Aseaza fileul de cod pe tava cu dovlecei, ardei si ceapa. Condimenteaza cu lamaie, usturoi si ierburi. Coace 20 min la 190°C.'},
            # Ziua 5
            {'nume': 'Budinca de Chia cu Fructe', 'tip': 'slabit', 'masa': 'mic_dejun', 'zi': 5, 'kcal': 280, 'proteine': 12, 'carbohidrati': 28, 'grasimi': 14,
             'img_url': 'https://images.unsplash.com/photo-1546548970-71785318a17b?w=400&h=300&fit=crop',
             'instructiuni': 'Amesteca 3 linguri seminte de chia cu 200ml lapte de migdale si putin miere. Lasa la frigider peste noapte. Dimineata adauga fructe proaspete.'},
            {'nume': 'Ou Fiert cu Rosie', 'tip': 'slabit', 'masa': 'gustare_1', 'zi': 5, 'kcal': 130, 'proteine': 10, 'carbohidrati': 5, 'grasimi': 8,
             'img_url': 'https://images.unsplash.com/photo-1482049016688-2d3e1b311543?w=400&h=300&fit=crop',
             'instructiuni': 'Fierbe 2 oua tari (10 min). Curata si serveste cu o rosie mare feliata, sare si piper.'},
            {'nume': 'Pui Teriyaki cu Orez Brun', 'tip': 'slabit', 'masa': 'pranz', 'zi': 5, 'kcal': 430, 'proteine': 34, 'carbohidrati': 40, 'grasimi': 12,
             'img_url': 'https://images.unsplash.com/photo-1569058242253-92a9c755a0ec?w=400&h=300&fit=crop',
             'instructiuni': 'Caleste piept de pui taiat cuburi in sos teriyaki light. Serveste cu orez brun fiert si broccoli aburit.'},
            {'nume': 'Smoothie de Afine', 'tip': 'slabit', 'masa': 'gustare_2', 'zi': 5, 'kcal': 140, 'proteine': 4, 'carbohidrati': 28, 'grasimi': 2,
             'img_url': 'https://images.unsplash.com/photo-1553530666-ba11a7da3888?w=400&h=300&fit=crop',
             'instructiuni': 'Mixeaza 100g afine congelate cu 150ml lapte de migdale si o lingurita de miere. Mixeaza pana devine cremos.'},
            {'nume': 'Salata de Ton cu Fasole', 'tip': 'slabit', 'masa': 'cina', 'zi': 5, 'kcal': 340, 'proteine': 30, 'carbohidrati': 22, 'grasimi': 14,
             'img_url': 'https://images.unsplash.com/photo-1540189549336-e6e99c3679fe?w=400&h=300&fit=crop',
             'instructiuni': 'Amesteca ton din conserva (scurs) cu fasole alba, ceapa rosie, patrunjel si rosii cherry. Dressing: ulei de masline si otet balsamic.'},
            # Ziua 6
            {'nume': 'Clatite de Ovaz cu Banane', 'tip': 'slabit', 'masa': 'mic_dejun', 'zi': 6, 'kcal': 310, 'proteine': 16, 'carbohidrati': 40, 'grasimi': 10,
             'img_url': 'https://images.unsplash.com/photo-1567620905732-2d1ec7ab7445?w=400&h=300&fit=crop',
             'instructiuni': 'Mixeaza 1 banana cu 2 oua si 40g fulgi de ovaz. Toarna in tigaia calda si coace pe ambele parti. Serveste cu putine fructe.'},
            {'nume': 'Ardei Umplut cu Branza', 'tip': 'slabit', 'masa': 'gustare_1', 'zi': 6, 'kcal': 130, 'proteine': 10, 'carbohidrati': 6, 'grasimi': 8,
             'img_url': 'https://images.unsplash.com/photo-1606923829579-0cb981a83e2e?w=400&h=300&fit=crop',
             'instructiuni': 'Taie un ardei pe jumatate, scoate semintele. Umple cu amestec de branza de vaci cu marar si usturoi.'},
            {'nume': 'Bowl Buddha cu Tofu', 'tip': 'slabit', 'masa': 'pranz', 'zi': 6, 'kcal': 410, 'proteine': 22, 'carbohidrati': 38, 'grasimi': 18,
             'img_url': 'https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=400&h=300&fit=crop',
             'instructiuni': 'Aseaza in bol: orez brun, tofu prajit, edamame, morcov ras, avocado si varza rosie. Dressing de susan.'},
            {'nume': 'Pepene Verde (200g)', 'tip': 'slabit', 'masa': 'gustare_2', 'zi': 6, 'kcal': 60, 'proteine': 1, 'carbohidrati': 15, 'grasimi': 0,
             'img_url': 'https://images.unsplash.com/photo-1563114773-84221bd62daa?w=400&h=300&fit=crop',
             'instructiuni': 'Taie 200g pepene verde in cuburi. Serveste rece. Perfect hidratant si cu putine calorii.'},
            {'nume': 'Pui cu Ciuperci si Legume', 'tip': 'slabit', 'masa': 'cina', 'zi': 6, 'kcal': 350, 'proteine': 34, 'carbohidrati': 12, 'grasimi': 16,
             'img_url': 'https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=400&h=300&fit=crop',
             'instructiuni': 'Caleste piept de pui in felii cu ciuperci champignon, ardei si dovlecei. Condimenteaza cu sos de soia light, usturoi si ghimbir.'},
            # Ziua 7
            {'nume': 'Avocado Toast cu Ou', 'tip': 'slabit', 'masa': 'mic_dejun', 'zi': 7, 'kcal': 340, 'proteine': 16, 'carbohidrati': 28, 'grasimi': 20,
             'img_url': 'https://images.unsplash.com/photo-1541519227354-08fa5d50c44d?w=400&h=300&fit=crop',
             'instructiuni': 'Prajeste o felie de paine integrala. Zdrobeste jumatate de avocado deasupra. Pune un ou ochi si presara fulgi de chili si sare.'},
            {'nume': 'Edamame (100g)', 'tip': 'slabit', 'masa': 'gustare_1', 'zi': 7, 'kcal': 120, 'proteine': 11, 'carbohidrati': 9, 'grasimi': 5,
             'img_url': 'https://images.unsplash.com/photo-1564894809611-1742fc40ed80?w=400&h=300&fit=crop',
             'instructiuni': 'Fierbe edamame congelate 5 min in apa sarata. Scurge si presara sare de mare.'},
            {'nume': 'Salata Greceasca cu Feta', 'tip': 'slabit', 'masa': 'pranz', 'zi': 7, 'kcal': 380, 'proteine': 16, 'carbohidrati': 18, 'grasimi': 26,
             'img_url': 'https://images.unsplash.com/photo-1540189549336-e6e99c3679fe?w=400&h=300&fit=crop',
             'instructiuni': 'Amesteca rosii, castraveti, ceapa rosie, masline si branza feta cuburi. Dressing: ulei de masline extravirgin, oregano si suc de lamaie.'},
            {'nume': 'Iaurt cu Scortisoara', 'tip': 'slabit', 'masa': 'gustare_2', 'zi': 7, 'kcal': 100, 'proteine': 10, 'carbohidrati': 8, 'grasimi': 3,
             'img_url': 'https://images.unsplash.com/photo-1488477181946-6428a0291777?w=400&h=300&fit=crop',
             'instructiuni': 'Pune 150g iaurt grecesc 0% intr-un bol. Presara scortisoara si un strop de miere.'},
            {'nume': 'Curry de Legume Light', 'tip': 'slabit', 'masa': 'cina', 'zi': 7, 'kcal': 300, 'proteine': 12, 'carbohidrati': 32, 'grasimi': 12,
             'img_url': 'https://images.unsplash.com/photo-1585937421612-70a008356fbe?w=400&h=300&fit=crop',
             'instructiuni': 'Caleste ceapa, usturoi si pasta curry. Adauga conopida, naut, spanac si lapte de cocos light. Gateste 15 min. Serveste cu orez basmati.'},

            # ========== MENTINERE (Echilibru) ~2200 kcal/zi ==========
            # Ziua 1
            {'nume': 'Sandwich Integral cu Ou si Avocado', 'tip': 'mentinere', 'masa': 'mic_dejun', 'zi': 1, 'kcal': 420, 'proteine': 22, 'carbohidrati': 38, 'grasimi': 22,
             'img_url': 'https://images.unsplash.com/photo-1525351484163-7529414344d8?w=400&h=300&fit=crop',
             'instructiuni': 'Prajeste painea integrala. Pune ou ochi, avocado feliat, rosie si rucola. Condimenteaza cu sare si piper.'},
            {'nume': 'Trail Mix (40g)', 'tip': 'mentinere', 'masa': 'gustare_1', 'zi': 1, 'kcal': 200, 'proteine': 6, 'carbohidrati': 18, 'grasimi': 13,
             'img_url': 'https://images.unsplash.com/photo-1604937455095-ef2fe3d46fcd?w=400&h=300&fit=crop',
             'instructiuni': 'Amesteca migdale, nuci caju, stafide si fulgi de cocos. Portie de 40g - o mana plina.'},
            {'nume': 'Paste Bolognese Clasice', 'tip': 'mentinere', 'masa': 'pranz', 'zi': 1, 'kcal': 580, 'proteine': 32, 'carbohidrati': 60, 'grasimi': 22,
             'img_url': 'https://images.unsplash.com/photo-1621996346565-e3dbc646d9a9?w=400&h=300&fit=crop',
             'instructiuni': 'Caleste ceapa si usturoiul. Adauga carne tocata de vita si prajeste. Pune bulion de rosii, oregano, busuioc. Fierbe 20 min. Serveste cu paste integrale al dente.'},
            {'nume': 'Banana cu Unt de Arahide', 'tip': 'mentinere', 'masa': 'gustare_2', 'zi': 1, 'kcal': 250, 'proteine': 8, 'carbohidrati': 30, 'grasimi': 12,
             'img_url': 'https://images.unsplash.com/photo-1571771894821-ce9b6c11b08e?w=400&h=300&fit=crop',
             'instructiuni': 'Taie banana in rondele. Adauga 2 linguri de unt de arahide natural si presara seminte de chia.'},
            {'nume': 'Salata Caesar cu Pui', 'tip': 'mentinere', 'masa': 'cina', 'zi': 1, 'kcal': 480, 'proteine': 35, 'carbohidrati': 22, 'grasimi': 28,
             'img_url': 'https://images.unsplash.com/photo-1550304943-4f24f54ddde9?w=400&h=300&fit=crop',
             'instructiuni': 'Rupe salata romaine. Adauga piept de pui la gratar feliat, crutoane integrale, parmezan si dressing Caesar light.'},
            # Ziua 2
            {'nume': 'Clatite Proteice cu Fructe', 'tip': 'mentinere', 'masa': 'mic_dejun', 'zi': 2, 'kcal': 450, 'proteine': 28, 'carbohidrati': 48, 'grasimi': 14,
             'img_url': 'https://images.unsplash.com/photo-1567620905732-2d1ec7ab7445?w=400&h=300&fit=crop',
             'instructiuni': 'Mixeaza 2 oua, 1 scoop whey, 50g ovaz si 100ml lapte. Coace clatitele in tigaia antiaderenta. Serveste cu capsuni si sirop de artar.'},
            {'nume': 'Branza de Vaci cu Rosii', 'tip': 'mentinere', 'masa': 'gustare_1', 'zi': 2, 'kcal': 160, 'proteine': 18, 'carbohidrati': 6, 'grasimi': 7,
             'img_url': 'https://images.unsplash.com/photo-1550304943-4f24f54ddde9?w=400&h=300&fit=crop',
             'instructiuni': 'Pune 150g branza de vaci intr-un bol. Adauga rosii cherry taiate, sare, piper si marar proaspat.'},
            {'nume': 'Friptura de Vita cu Piure', 'tip': 'mentinere', 'masa': 'pranz', 'zi': 2, 'kcal': 620, 'proteine': 40, 'carbohidrati': 45, 'grasimi': 28,
             'img_url': 'https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=400&h=300&fit=crop',
             'instructiuni': 'Gateste friptura la gratar sau tigaie 4 min pe parte (medium). Serveste cu piure de cartofi facut cu unt si lapte cald. Adauga legume la abur.'},
            {'nume': 'Iaurt cu Granola si Miere', 'tip': 'mentinere', 'masa': 'gustare_2', 'zi': 2, 'kcal': 220, 'proteine': 12, 'carbohidrati': 30, 'grasimi': 7,
             'img_url': 'https://images.unsplash.com/photo-1495214783159-3503fd1b572d?w=400&h=300&fit=crop',
             'instructiuni': 'Pune iaurt grecesc intr-un bol. Adauga 40g granola, un fir de miere si fructe de padure.'},
            {'nume': 'Tacos cu Peste si Salsa', 'tip': 'mentinere', 'masa': 'cina', 'zi': 2, 'kcal': 520, 'proteine': 30, 'carbohidrati': 42, 'grasimi': 24,
             'img_url': 'https://images.unsplash.com/photo-1565299585323-38d6b0865b47?w=400&h=300&fit=crop',
             'instructiuni': 'Prajeste fileul de peste alb cu condimente mexicane. Pune in tortilla cu varza, salsa de rosii, avocado si smantana.'},
            # Ziua 3
            {'nume': 'Overnight Oats cu Fructe', 'tip': 'mentinere', 'masa': 'mic_dejun', 'zi': 3, 'kcal': 400, 'proteine': 16, 'carbohidrati': 52, 'grasimi': 14,
             'img_url': 'https://images.unsplash.com/photo-1517673400267-0251440c45dc?w=400&h=300&fit=crop',
             'instructiuni': 'Seara: amesteca 60g ovaz, 200ml lapte, 1 lingura seminte chia, miere. Dimineata adauga fructe proaspete si nuci.'},
            {'nume': 'Baton Proteic si Mar', 'tip': 'mentinere', 'masa': 'gustare_1', 'zi': 3, 'kcal': 230, 'proteine': 20, 'carbohidrati': 22, 'grasimi': 8,
             'img_url': 'https://images.unsplash.com/photo-1622484212850-eb596d769edc?w=400&h=300&fit=crop',
             'instructiuni': 'Un baton proteic cu minim 20g proteine si un mar mediu verde. Gustare rapida si echilibrata.'},
            {'nume': 'Risotto cu Ciuperci', 'tip': 'mentinere', 'masa': 'pranz', 'zi': 3, 'kcal': 560, 'proteine': 18, 'carbohidrati': 65, 'grasimi': 24,
             'img_url': 'https://images.unsplash.com/photo-1476124369491-e7addf5db371?w=400&h=300&fit=crop',
             'instructiuni': 'Caleste ceapa in unt, adauga orez arborio si amesteca. Pune polonic cu polonic supa calda, amestecand constant. Adauga ciuperci calite si parmezan.'},
            {'nume': 'Smoothie cu Avocado si Cacao', 'tip': 'mentinere', 'masa': 'gustare_2', 'zi': 3, 'kcal': 240, 'proteine': 8, 'carbohidrati': 22, 'grasimi': 15,
             'img_url': 'https://images.unsplash.com/photo-1638176066666-ffb2f013c7dd?w=400&h=300&fit=crop',
             'instructiuni': 'Mixeaza jumatate avocado, 1 lingura cacao, banana, 200ml lapte de migdale si putin miere.'},
            {'nume': 'Pui la Cuptor cu Cartofi', 'tip': 'mentinere', 'masa': 'cina', 'zi': 3, 'kcal': 550, 'proteine': 38, 'carbohidrati': 40, 'grasimi': 22,
             'img_url': 'https://images.unsplash.com/photo-1598515214211-89d3c73ae83b?w=400&h=300&fit=crop',
             'instructiuni': 'Condimenteaza pulpa de pui cu boia, rozmarin si usturoi. Pune pe tava cu cartofi taiati. Stropeste cu ulei si coace 45 min la 200°C.'},
            # Ziua 4
            {'nume': 'Omleta cu Branza si Ciuperci', 'tip': 'mentinere', 'masa': 'mic_dejun', 'zi': 4, 'kcal': 400, 'proteine': 28, 'carbohidrati': 10, 'grasimi': 28,
             'img_url': 'https://images.unsplash.com/photo-1510693206972-df098062cb71?w=400&h=300&fit=crop',
             'instructiuni': 'Bate 3 oua. Caleste ciupercile in tigaie. Toarna ouale, presara branza rasa si impatureste cand e gata.'},
            {'nume': 'Hummus cu Pita Integrala', 'tip': 'mentinere', 'masa': 'gustare_1', 'zi': 4, 'kcal': 240, 'proteine': 10, 'carbohidrati': 28, 'grasimi': 12,
             'img_url': 'https://images.unsplash.com/photo-1613478881427-d31e0f514623?w=400&h=300&fit=crop',
             'instructiuni': 'Taie pita integrala in triunghiuri. Serveste cu 4 linguri de hummus clasic si bete de morcov.'},
            {'nume': 'Bowl Mexicano cu Orez', 'tip': 'mentinere', 'masa': 'pranz', 'zi': 4, 'kcal': 600, 'proteine': 32, 'carbohidrati': 58, 'grasimi': 24,
             'img_url': 'https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=400&h=300&fit=crop',
             'instructiuni': 'Pune in bol: orez, fasole neagra, porumb, pui calite cu condimente mexicane, avocado, salsa si smantana.'},
            {'nume': 'Nuci si Fructe Uscate', 'tip': 'mentinere', 'masa': 'gustare_2', 'zi': 4, 'kcal': 200, 'proteine': 5, 'carbohidrati': 20, 'grasimi': 12,
             'img_url': 'https://images.unsplash.com/photo-1604937455095-ef2fe3d46fcd?w=400&h=300&fit=crop',
             'instructiuni': 'Mix de 20g nuci, 10g stafide si 10g caise uscate. Portie controlata pentru energie sustinuta.'},
            {'nume': 'Somon cu Sos de Lamaie', 'tip': 'mentinere', 'masa': 'cina', 'zi': 4, 'kcal': 480, 'proteine': 36, 'carbohidrati': 18, 'grasimi': 28,
             'img_url': 'https://images.unsplash.com/photo-1467003909585-2f8a72700288?w=400&h=300&fit=crop',
             'instructiuni': 'Coace somonul 15 min la 200°C. Pregateste sos de lamaie cu unt si capere. Serveste cu sparanghel la abur.'},
            # Ziua 5
            {'nume': 'Porridge cu Mere si Scortisoara', 'tip': 'mentinere', 'masa': 'mic_dejun', 'zi': 5, 'kcal': 380, 'proteine': 14, 'carbohidrati': 55, 'grasimi': 12,
             'img_url': 'https://images.unsplash.com/photo-1517673400267-0251440c45dc?w=400&h=300&fit=crop',
             'instructiuni': 'Fierbe 60g fulgi de ovaz in lapte 5 min. Adauga mar ras, scortisoara, nuci si un fir de miere.'},
            {'nume': 'Ou Fiert cu Avocado', 'tip': 'mentinere', 'masa': 'gustare_1', 'zi': 5, 'kcal': 200, 'proteine': 10, 'carbohidrati': 6, 'grasimi': 16,
             'img_url': 'https://images.unsplash.com/photo-1482049016688-2d3e1b311543?w=400&h=300&fit=crop',
             'instructiuni': 'Fierbe 2 oua tari. Taie pe jumatate si serveste cu sfert de avocado, sare si piper.'},
            {'nume': 'Burger de Pui cu Salata', 'tip': 'mentinere', 'masa': 'pranz', 'zi': 5, 'kcal': 580, 'proteine': 36, 'carbohidrati': 42, 'grasimi': 26,
             'img_url': 'https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=400&h=300&fit=crop',
             'instructiuni': 'Formeaza chiftea din piept de pui tocat cu condimente. Prajeste in tigaie. Serveste in chifluta integrala cu salata, rosie si sos de mustar.'},
            {'nume': 'Batoane de Cereale', 'tip': 'mentinere', 'masa': 'gustare_2', 'zi': 5, 'kcal': 180, 'proteine': 5, 'carbohidrati': 28, 'grasimi': 7,
             'img_url': 'https://images.unsplash.com/photo-1622484212850-eb596d769edc?w=400&h=300&fit=crop',
             'instructiuni': 'Un baton de cereale cu ovaz, miere si fructe uscate. Gustare practica pentru energie rapida.'},
            {'nume': 'Paste cu Pesto si Pui', 'tip': 'mentinere', 'masa': 'cina', 'zi': 5, 'kcal': 540, 'proteine': 34, 'carbohidrati': 50, 'grasimi': 22,
             'img_url': 'https://images.unsplash.com/photo-1621996346565-e3dbc646d9a9?w=400&h=300&fit=crop',
             'instructiuni': 'Fierbe paste integrale al dente. Caleste pieptul de pui. Amesteca cu pesto de busuioc, rosii cherry si parmezan.'},
            # Ziua 6
            {'nume': 'Toast Frantuzesc cu Fructe', 'tip': 'mentinere', 'masa': 'mic_dejun', 'zi': 6, 'kcal': 430, 'proteine': 18, 'carbohidrati': 48, 'grasimi': 18,
             'img_url': 'https://images.unsplash.com/photo-1484723091739-30a097e8f929?w=400&h=300&fit=crop',
             'instructiuni': 'Inmoaie felii de paine in amestec de ou, lapte si scortisoara. Prajeste in tigaie cu putin unt. Serveste cu fructe si sirop de artar.'},
            {'nume': 'Mix de Fructe Proaspete', 'tip': 'mentinere', 'masa': 'gustare_1', 'zi': 6, 'kcal': 150, 'proteine': 2, 'carbohidrati': 35, 'grasimi': 1,
             'img_url': 'https://images.unsplash.com/photo-1490474418585-ba9bad8fd0ea?w=400&h=300&fit=crop',
             'instructiuni': 'Taie capsuni, kiwi, mango si afine intr-un bol. Stoarce putin suc de portocala deasupra.'},
            {'nume': 'Gyros cu Pui si Tzatziki', 'tip': 'mentinere', 'masa': 'pranz', 'zi': 6, 'kcal': 560, 'proteine': 34, 'carbohidrati': 45, 'grasimi': 24,
             'img_url': 'https://images.unsplash.com/photo-1626700051175-6818013e1d4f?w=400&h=300&fit=crop',
             'instructiuni': 'Condimenteaza pui cu oregano, boia si usturoi. Caleste si pune in lipie cu salata, rosii, ceapa si sos tzatziki.'},
            {'nume': 'Branza cu Biscuiti Integrali', 'tip': 'mentinere', 'masa': 'gustare_2', 'zi': 6, 'kcal': 190, 'proteine': 10, 'carbohidrati': 20, 'grasimi': 8,
             'img_url': 'https://images.unsplash.com/photo-1486297678162-eb2a19b0a32d?w=400&h=300&fit=crop',
             'instructiuni': 'Serveste 4 biscuiti integrali cu branza Gouda sau Emmental feliata subtire.'},
            {'nume': 'Tocanita de Legume cu Carne', 'tip': 'mentinere', 'masa': 'cina', 'zi': 6, 'kcal': 500, 'proteine': 32, 'carbohidrati': 35, 'grasimi': 24,
             'img_url': 'https://images.unsplash.com/photo-1585937421612-70a008356fbe?w=400&h=300&fit=crop',
             'instructiuni': 'Caleste ceapa si carnea de vita cuburi. Adauga cartofi, morcovi, ardei si bulion. Fierbe la foc mic 40 min pana se inmoaie carnea.'},
            # Ziua 7
            {'nume': 'Acai Bowl cu Topping', 'tip': 'mentinere', 'masa': 'mic_dejun', 'zi': 7, 'kcal': 420, 'proteine': 12, 'carbohidrati': 55, 'grasimi': 18,
             'img_url': 'https://images.unsplash.com/photo-1590301157890-4810ed352733?w=400&h=300&fit=crop',
             'instructiuni': 'Mixeaza pulpa de acai congelata cu banana si putin lapte. Toarna in bol si adauga granola, cocos, fructe si miere.'},
            {'nume': 'Crackers cu Avocado', 'tip': 'mentinere', 'masa': 'gustare_1', 'zi': 7, 'kcal': 210, 'proteine': 4, 'carbohidrati': 18, 'grasimi': 14,
             'img_url': 'https://images.unsplash.com/photo-1541519227354-08fa5d50c44d?w=400&h=300&fit=crop',
             'instructiuni': 'Intinde avocado zdrobit pe 4 crackers integrali. Presara sare, piper si fulgi de chili.'},
            {'nume': 'Sushi Bowl Homemade', 'tip': 'mentinere', 'masa': 'pranz', 'zi': 7, 'kcal': 560, 'proteine': 28, 'carbohidrati': 60, 'grasimi': 20,
             'img_url': 'https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=400&h=300&fit=crop',
             'instructiuni': 'Pune in bol orez sushi cu otet de orez, somon afumat, avocado, castravete, edamame si sos de soia cu wasabi.'},
            {'nume': 'Ciocolata Neagra (20g)', 'tip': 'mentinere', 'masa': 'gustare_2', 'zi': 7, 'kcal': 110, 'proteine': 2, 'carbohidrati': 10, 'grasimi': 8,
             'img_url': 'https://images.unsplash.com/photo-1606312619070-d48b4c652a52?w=400&h=300&fit=crop',
             'instructiuni': '20g ciocolata neagra minim 70% cacao. Savureaza incet, bucata cu bucata.'},
            {'nume': 'Pizza Integrala cu Legume', 'tip': 'mentinere', 'masa': 'cina', 'zi': 7, 'kcal': 520, 'proteine': 24, 'carbohidrati': 52, 'grasimi': 22,
             'img_url': 'https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=400&h=300&fit=crop',
             'instructiuni': 'Intinde blatul integral. Pune sos de rosii, mozzarella, ardei, ciuperci, masline si rucola. Coace 12-15 min la 220°C.'},

            # ========== INGRASARE (Masa Musculara) ~3000 kcal/zi ==========
            # Ziua 1
            {'nume': 'Porridge Proteic cu Arahide', 'tip': 'ingrasare', 'masa': 'mic_dejun', 'zi': 1, 'kcal': 620, 'proteine': 32, 'carbohidrati': 65, 'grasimi': 24,
             'img_url': 'https://images.unsplash.com/photo-1517673400267-0251440c45dc?w=400&h=300&fit=crop',
             'instructiuni': 'Fierbe 80g fulgi de ovaz in lapte integral. Adauga 1 scoop whey, 2 linguri unt de arahide, banana feliata si miere.'},
            {'nume': 'Shake Masa cu Banana si Ovaz', 'tip': 'ingrasare', 'masa': 'gustare_1', 'zi': 1, 'kcal': 450, 'proteine': 30, 'carbohidrati': 55, 'grasimi': 14,
             'img_url': 'https://images.unsplash.com/photo-1638176066666-ffb2f013c7dd?w=400&h=300&fit=crop',
             'instructiuni': 'Mixeaza 2 banane, 50g ovaz, 1 scoop whey, 300ml lapte integral si 1 lingura miere. Mixeaza 90 secunde.'},
            {'nume': 'Burger de Vita cu Cartofi Dulci', 'tip': 'ingrasare', 'masa': 'pranz', 'zi': 1, 'kcal': 780, 'proteine': 42, 'carbohidrati': 65, 'grasimi': 34,
             'img_url': 'https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=400&h=300&fit=crop',
             'instructiuni': 'Formeaza chiftea din carne de vita tocata cu condimente. Prajeste si pune in chifluta brioche cu salata, branza si sos. Serveste cu cartofi dulci la cuptor.'},
            {'nume': 'Budinca de Orez cu Proteina', 'tip': 'ingrasare', 'masa': 'gustare_2', 'zi': 1, 'kcal': 380, 'proteine': 24, 'carbohidrati': 50, 'grasimi': 10,
             'img_url': 'https://images.unsplash.com/photo-1488477181946-6428a0291777?w=400&h=300&fit=crop',
             'instructiuni': 'Fierbe orez cu lapte integral si vanilie. Lasa sa se raceasca putin si amesteca 1 scoop whey. Serveste cu scortisoara.'},
            {'nume': 'Steak cu Orez si Broccoli', 'tip': 'ingrasare', 'masa': 'cina', 'zi': 1, 'kcal': 720, 'proteine': 48, 'carbohidrati': 55, 'grasimi': 30,
             'img_url': 'https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=400&h=300&fit=crop',
             'instructiuni': 'Gateste steak de vita medium-rare (4 min pe parte). Serveste cu orez alb si broccoli aburit. Topping: unt cu usturoi.'},
            # Ziua 2
            {'nume': 'Oua Jumari cu Branza si Paine', 'tip': 'ingrasare', 'masa': 'mic_dejun', 'zi': 2, 'kcal': 580, 'proteine': 34, 'carbohidrati': 35, 'grasimi': 34,
             'img_url': 'https://images.unsplash.com/photo-1510693206972-df098062cb71?w=400&h=300&fit=crop',
             'instructiuni': 'Bate 4 oua si gateste scrambled eggs cu branza Cheddar rasa. Serveste cu 2 felii de paine prajita cu unt.'},
            {'nume': 'Wrap cu Unt de Arahide si Banana', 'tip': 'ingrasare', 'masa': 'gustare_1', 'zi': 2, 'kcal': 420, 'proteine': 14, 'carbohidrati': 50, 'grasimi': 20,
             'img_url': 'https://images.unsplash.com/photo-1626700051175-6818013e1d4f?w=400&h=300&fit=crop',
             'instructiuni': 'Intinde 2 linguri unt de arahide pe tortilla. Pune banana feliata si presara scortisoara. Ruleaza si serveste.'},
            {'nume': 'Pui cu Paste si Sos Alfredo', 'tip': 'ingrasare', 'masa': 'pranz', 'zi': 2, 'kcal': 750, 'proteine': 45, 'carbohidrati': 60, 'grasimi': 32,
             'img_url': 'https://images.unsplash.com/photo-1621996346565-e3dbc646d9a9?w=400&h=300&fit=crop',
             'instructiuni': 'Fierbe paste penne. Caleste piept de pui taiat cuburi. Pregateste sos Alfredo din smantana, parmezan si unt. Amesteca totul.'},
            {'nume': 'Smoothie Caloric cu Ovaz', 'tip': 'ingrasare', 'masa': 'gustare_2', 'zi': 2, 'kcal': 400, 'proteine': 28, 'carbohidrati': 48, 'grasimi': 12,
             'img_url': 'https://images.unsplash.com/photo-1553530666-ba11a7da3888?w=400&h=300&fit=crop',
             'instructiuni': 'Mixeaza 1 banana, 40g ovaz, 1 scoop whey, 1 lingura unt de migdale, 250ml lapte integral.'},
            {'nume': 'Somon cu Piure si Unt', 'tip': 'ingrasare', 'masa': 'cina', 'zi': 2, 'kcal': 700, 'proteine': 42, 'carbohidrati': 45, 'grasimi': 36,
             'img_url': 'https://images.unsplash.com/photo-1467003909585-2f8a72700288?w=400&h=300&fit=crop',
             'instructiuni': 'Coace somon 18 min la 200°C. Pregateste piure de cartofi cu unt si lapte integral. Serveste cu sparanghel si sos de lamaie.'},
            # Ziua 3
            {'nume': 'Granola cu Lapte si Banane', 'tip': 'ingrasare', 'masa': 'mic_dejun', 'zi': 3, 'kcal': 550, 'proteine': 18, 'carbohidrati': 72, 'grasimi': 22,
             'img_url': 'https://images.unsplash.com/photo-1495214783159-3503fd1b572d?w=400&h=300&fit=crop',
             'instructiuni': 'Pune 80g granola intr-un bol cu 250ml lapte integral. Adauga banana feliata, nuci si miere.'},
            {'nume': 'Sandvis cu Pui si Avocado', 'tip': 'ingrasare', 'masa': 'gustare_1', 'zi': 3, 'kcal': 450, 'proteine': 28, 'carbohidrati': 35, 'grasimi': 22,
             'img_url': 'https://images.unsplash.com/photo-1525351484163-7529414344d8?w=400&h=300&fit=crop',
             'instructiuni': 'Pune piept de pui feliat pe paine integrala cu avocado, rosie, salata si maioneza light. Inchide sandvisul.'},
            {'nume': 'Chili con Carne cu Orez', 'tip': 'ingrasare', 'masa': 'pranz', 'zi': 3, 'kcal': 780, 'proteine': 42, 'carbohidrati': 70, 'grasimi': 30,
             'img_url': 'https://images.unsplash.com/photo-1585937421612-70a008356fbe?w=400&h=300&fit=crop',
             'instructiuni': 'Caleste carne tocata cu ceapa si ardei. Adauga fasole rosie, rosii conserva si condimente chili. Fierbe 25 min. Serveste cu orez si smantana.'},
            {'nume': 'Budinca Proteica cu Ciocolata', 'tip': 'ingrasare', 'masa': 'gustare_2', 'zi': 3, 'kcal': 350, 'proteine': 30, 'carbohidrati': 35, 'grasimi': 10,
             'img_url': 'https://images.unsplash.com/photo-1606312619070-d48b4c652a52?w=400&h=300&fit=crop',
             'instructiuni': 'Amesteca 1 scoop whey ciocolata cu 200ml lapte, 1 banana si cacao. Mixeaza si serveste in bol cu topping de granola.'},
            {'nume': 'Paste Carbonara cu Bacon', 'tip': 'ingrasare', 'masa': 'cina', 'zi': 3, 'kcal': 750, 'proteine': 38, 'carbohidrati': 60, 'grasimi': 38,
             'img_url': 'https://images.unsplash.com/photo-1621996346565-e3dbc646d9a9?w=400&h=300&fit=crop',
             'instructiuni': 'Fierbe spaghetti. Prajeste bacon si amesteca oua cu pecorino. Combina pastele cu bacon si sosul cremos. Condimenteaza cu piper.'},
            # Ziua 4
            {'nume': 'Pancakes cu Proteina si Sirop', 'tip': 'ingrasare', 'masa': 'mic_dejun', 'zi': 4, 'kcal': 600, 'proteine': 35, 'carbohidrati': 65, 'grasimi': 20,
             'img_url': 'https://images.unsplash.com/photo-1567620905732-2d1ec7ab7445?w=400&h=300&fit=crop',
             'instructiuni': 'Mixeaza 2 oua, 1 scoop whey, 60g ovaz si lapte. Coace pancakes si serveste cu sirop de artar, unt si fructe.'},
            {'nume': 'Sandwich cu Ton si Branza', 'tip': 'ingrasare', 'masa': 'gustare_1', 'zi': 4, 'kcal': 400, 'proteine': 30, 'carbohidrati': 32, 'grasimi': 18,
             'img_url': 'https://images.unsplash.com/photo-1525351484163-7529414344d8?w=400&h=300&fit=crop',
             'instructiuni': 'Amesteca ton cu maioneza si pune pe paine integrala cu branza topita. Adauga salata verde si rosie.'},
            {'nume': 'Shawarma de Pui cu Cartofi', 'tip': 'ingrasare', 'masa': 'pranz', 'zi': 4, 'kcal': 800, 'proteine': 44, 'carbohidrati': 65, 'grasimi': 36,
             'img_url': 'https://images.unsplash.com/photo-1626700051175-6818013e1d4f?w=400&h=300&fit=crop',
             'instructiuni': 'Condimenteaza pui cu chimion, curcuma si boia. Caleste si pune in lipie cu hummus, salata, ceapa si sos tahini. Serveste cu cartofi prajiti.'},
            {'nume': 'Fulgi de Ovaz cu Lapte si Unt', 'tip': 'ingrasare', 'masa': 'gustare_2', 'zi': 4, 'kcal': 380, 'proteine': 15, 'carbohidrati': 50, 'grasimi': 14,
             'img_url': 'https://images.unsplash.com/photo-1517673400267-0251440c45dc?w=400&h=300&fit=crop',
             'instructiuni': 'Fierbe 60g fulgi de ovaz in lapte integral. Adauga 1 lingura unt de arahide, banana si miere.'},
            {'nume': 'Pui Intreg la Cuptor cu Legume', 'tip': 'ingrasare', 'masa': 'cina', 'zi': 4, 'kcal': 700, 'proteine': 50, 'carbohidrati': 40, 'grasimi': 34,
             'img_url': 'https://images.unsplash.com/photo-1598515214211-89d3c73ae83b?w=400&h=300&fit=crop',
             'instructiuni': 'Condimenteaza pulpa de pui cu rozmarin, usturoi si boia. Pune pe tava cu cartofi si morcovi. Stropeste cu ulei si coace 50 min la 200°C.'},
            # Ziua 5
            {'nume': 'French Toast cu Banana si Miere', 'tip': 'ingrasare', 'masa': 'mic_dejun', 'zi': 5, 'kcal': 580, 'proteine': 24, 'carbohidrati': 65, 'grasimi': 24,
             'img_url': 'https://images.unsplash.com/photo-1484723091739-30a097e8f929?w=400&h=300&fit=crop',
             'instructiuni': 'Inmoaie 3 felii de brioche in amestec de ou, lapte si vanilie. Prajeste in unt. Serveste cu banana, miere si nuci.'},
            {'nume': 'Shake de Masa Ciocolata', 'tip': 'ingrasare', 'masa': 'gustare_1', 'zi': 5, 'kcal': 480, 'proteine': 35, 'carbohidrati': 50, 'grasimi': 16,
             'img_url': 'https://images.unsplash.com/photo-1553530666-ba11a7da3888?w=400&h=300&fit=crop',
             'instructiuni': 'Mixeaza 1 scoop whey ciocolata, 1 banana, 50g ovaz, 1 lingura unt de arahide, 300ml lapte integral si gheata.'},
            {'nume': 'Burrito cu Carne si Fasole', 'tip': 'ingrasare', 'masa': 'pranz', 'zi': 5, 'kcal': 800, 'proteine': 40, 'carbohidrati': 70, 'grasimi': 34,
             'img_url': 'https://images.unsplash.com/photo-1626700051175-6818013e1d4f?w=400&h=300&fit=crop',
             'instructiuni': 'Caleste carne tocata cu condimente mexicane. Pune pe tortilla mare cu fasole, orez, branza rasa, guacamole si smantana. Ruleaza strans.'},
            {'nume': 'Iaurt cu Granola si Unt de Arahide', 'tip': 'ingrasare', 'masa': 'gustare_2', 'zi': 5, 'kcal': 400, 'proteine': 22, 'carbohidrati': 40, 'grasimi': 18,
             'img_url': 'https://images.unsplash.com/photo-1495214783159-3503fd1b572d?w=400&h=300&fit=crop',
             'instructiuni': 'Pune 200g iaurt grecesc, 50g granola, 1 lingura unt de arahide si miere. Amesteca usor.'},
            {'nume': 'Cotlet de Porc cu Cartofi', 'tip': 'ingrasare', 'masa': 'cina', 'zi': 5, 'kcal': 720, 'proteine': 45, 'carbohidrati': 50, 'grasimi': 36,
             'img_url': 'https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=400&h=300&fit=crop',
             'instructiuni': 'Condimenteaza cotletul cu sare, piper si rozmarin. Gateste 5 min pe parte. Serveste cu cartofi la cuptor si sos de mustar.'},
            # Ziua 6
            {'nume': 'Bowl de Acai cu Granola', 'tip': 'ingrasare', 'masa': 'mic_dejun', 'zi': 6, 'kcal': 560, 'proteine': 16, 'carbohidrati': 72, 'grasimi': 24,
             'img_url': 'https://images.unsplash.com/photo-1590301157890-4810ed352733?w=400&h=300&fit=crop',
             'instructiuni': 'Mixeaza pulpa acai cu banana si putin lapte. Toarna in bol, adauga 60g granola, banana, cocos, unt de arahide si miere.'},
            {'nume': 'Sandwich Dublu cu Ou si Branza', 'tip': 'ingrasare', 'masa': 'gustare_1', 'zi': 6, 'kcal': 450, 'proteine': 26, 'carbohidrati': 38, 'grasimi': 22,
             'img_url': 'https://images.unsplash.com/photo-1525351484163-7529414344d8?w=400&h=300&fit=crop',
             'instructiuni': 'Prajeste 2 felii paine. Pune 2 oua ochi si 2 felii branza. Inchide sandvisul si apasa usor.'},
            {'nume': 'Pui la Wok cu Noodles', 'tip': 'ingrasare', 'masa': 'pranz', 'zi': 6, 'kcal': 750, 'proteine': 40, 'carbohidrati': 70, 'grasimi': 30,
             'img_url': 'https://images.unsplash.com/photo-1569058242253-92a9c755a0ec?w=400&h=300&fit=crop',
             'instructiuni': 'Caleste pui cu legume (ardei, morcov, broccoli) la foc mare. Adauga noodles fierte si sos de soia cu usturoi si ghimbir.'},
            {'nume': 'Orez cu Lapte si Scortisoara', 'tip': 'ingrasare', 'masa': 'gustare_2', 'zi': 6, 'kcal': 350, 'proteine': 10, 'carbohidrati': 55, 'grasimi': 10,
             'img_url': 'https://images.unsplash.com/photo-1488477181946-6428a0291777?w=400&h=300&fit=crop',
             'instructiuni': 'Fierbe orezul in lapte integral cu zahar si coaja de lamaie 25 min. Serveste cald cu scortisoara presarata.'},
            {'nume': 'Pizza cu Carne si Mozzarella', 'tip': 'ingrasare', 'masa': 'cina', 'zi': 6, 'kcal': 780, 'proteine': 40, 'carbohidrati': 65, 'grasimi': 36,
             'img_url': 'https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=400&h=300&fit=crop',
             'instructiuni': 'Intinde blatul de pizza. Pune sos de rosii, mozzarella din belsug, carne tocata calita, ardei si ceapa. Coace 15 min la 220°C.'},
            # Ziua 7
            {'nume': 'Mic Dejun Englez Complet', 'tip': 'ingrasare', 'masa': 'mic_dejun', 'zi': 7, 'kcal': 650, 'proteine': 35, 'carbohidrati': 45, 'grasimi': 36,
             'img_url': 'https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=400&h=300&fit=crop',
             'instructiuni': 'Prajeste 3 oua, bacon, ciuperci si rosii in tigaie. Serveste cu fasole la conserva in sos de rosii, toast si unt.'},
            {'nume': 'Smoothie Bowl cu Proteina', 'tip': 'ingrasare', 'masa': 'gustare_1', 'zi': 7, 'kcal': 450, 'proteine': 30, 'carbohidrati': 50, 'grasimi': 14,
             'img_url': 'https://images.unsplash.com/photo-1590301157890-4810ed352733?w=400&h=300&fit=crop',
             'instructiuni': 'Mixeaza 1 scoop whey cu banana congelata si lapte (putin, sa fie gros). Pune in bol cu granola, fructe si seminte.'},
            {'nume': 'Kebab cu Orez si Hummus', 'tip': 'ingrasare', 'masa': 'pranz', 'zi': 7, 'kcal': 800, 'proteine': 42, 'carbohidrati': 70, 'grasimi': 34,
             'img_url': 'https://images.unsplash.com/photo-1626700051175-6818013e1d4f?w=400&h=300&fit=crop',
             'instructiuni': 'Pregateste kebab din carne tocata de miel cu condimente. Gateste la gratar. Serveste cu orez, hummus, salata si sos de iaurt.'},
            {'nume': 'Unt de Arahide pe Toast cu Miere', 'tip': 'ingrasare', 'masa': 'gustare_2', 'zi': 7, 'kcal': 380, 'proteine': 12, 'carbohidrati': 40, 'grasimi': 20,
             'img_url': 'https://images.unsplash.com/photo-1525351484163-7529414344d8?w=400&h=300&fit=crop',
             'instructiuni': 'Prajeste 2 felii de paine integrala. Intinde 2 linguri unt de arahide si adauga un fir de miere si felii de banana.'},
            {'nume': 'Musaca Romaneasca', 'tip': 'ingrasare', 'masa': 'cina', 'zi': 7, 'kcal': 720, 'proteine': 38, 'carbohidrati': 50, 'grasimi': 38,
             'img_url': 'https://images.unsplash.com/photo-1585937421612-70a008356fbe?w=400&h=300&fit=crop',
             'instructiuni': 'Caleste carne tocata cu ceapa. Pune straturi de cartofi fierti si carne intr-o tava. Toarna deasupra amestec de smantana cu oua. Coace 30 min la 200°C.'},
        ]
        for r in retete:
            Reteta.objects.create(**r)
        self.stdout.write(self.style.SUCCESS(f'Retete index: {Reteta.objects.count()}'))

    def _seed_exercitii_index(self):
        self.stdout.write('--- Exercitii pt pagina landing ---')
        Exercitiu.objects.all().delete()
        # 3 diete x 7 zile = 21 exercitii zilnice (cu variante acasa/sala/aer_liber)
        exercitii = [
            # ========== SLABIT - 7 ZILE ==========
            # Ziua 1 - HIIT Full Body
            {'titlu': 'HIIT Full Body - Ardere Maxima', 'locatie': 'acasa', 'obiectiv': 'slabit', 'zi': 1, 'durata_minute': 25,
             'descriere': 'Burpees, mountain climbers, jumping jacks, high knees, squat jumps. 40s lucru, 20s pauza. 4 runde cu 1 min pauza intre runde.',
             'tag': 'HIIT, Cardio', 'img_url': 'https://images.unsplash.com/photo-1517836357463-d25dfeac3438?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=ml6cT4AZdqI'},
            {'titlu': 'Circuit Cardio la Sala', 'locatie': 'sala', 'obiectiv': 'slabit', 'zi': 1, 'durata_minute': 40,
             'descriere': 'Bicicleta 5min, ramat 12rep, press piept 12rep, extensii picioare 15rep, banda 5min. 4 runde, pauza minima 30s.',
             'tag': 'Circuit, Cardio', 'img_url': 'https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=UItWltVZZmE'},
            {'titlu': 'Alergare Intervale in Parc', 'locatie': 'aer_liber', 'obiectiv': 'slabit', 'zi': 1, 'durata_minute': 35,
             'descriere': '1 min sprint, 2 min mers rapid. 10 repetari. Incalzire 5 min, racire 5 min. Arde 400-500 kcal.',
             'tag': 'Cardio, HIIT', 'img_url': 'https://images.unsplash.com/photo-1476480862126-209bfaa8edc8?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=CBWQGb4LyAM'},
            # Ziua 2 - Picioare si Core
            {'titlu': 'Picioare si Core Acasa', 'locatie': 'acasa', 'obiectiv': 'slabit', 'zi': 2, 'durata_minute': 30,
             'descriere': 'Genuflexiuni 4x15, fandari 3x12, glute bridges 3x20, plank 3x45s, bicycle crunch 3x20. Fara echipament.',
             'tag': 'Tonifiere, Core', 'img_url': 'https://images.unsplash.com/photo-1571019614242-c5c5dee9f50b?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=UItWltVZZmE'},
            {'titlu': 'Leg Day Ardere la Sala', 'locatie': 'sala', 'obiectiv': 'slabit', 'zi': 2, 'durata_minute': 45,
             'descriere': 'Leg press 3x15, leg extension 3x15, leg curl 3x15, calf raises 3x20, ab crunch machine 3x15. Greutati moderate.',
             'tag': 'Tonifiere, Forta', 'img_url': 'https://images.unsplash.com/photo-1574680096145-d05b474e2155?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=tBzbv4KcJRU'},
            {'titlu': 'Mers Rapid cu Pante', 'locatie': 'aer_liber', 'obiectiv': 'slabit', 'zi': 2, 'durata_minute': 45,
             'descriere': 'Mers rapid 6-7 km/h pe teren cu pante. Foloseste muntele sau scarile din parc. Arde 350 kcal fara impact.',
             'tag': 'Cardio', 'img_url': 'https://images.unsplash.com/photo-1551698618-1dfe5d97d256?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=CBWQGb4LyAM'},
            # Ziua 3 - Upper Body + Cardio
            {'titlu': 'Flotari si Cardio Mix', 'locatie': 'acasa', 'obiectiv': 'slabit', 'zi': 3, 'durata_minute': 25,
             'descriere': 'Flotari 4x12, plank jacks 3x30s, diamond push-ups 3x10, jumping jacks 3x30s, superman 3x15.',
             'tag': 'HIIT, Forta', 'img_url': 'https://images.unsplash.com/photo-1598971639058-fab3c3109a00?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=ml6cT4AZdqI'},
            {'titlu': 'Cardio + Greutati Upper', 'locatie': 'sala', 'obiectiv': 'slabit', 'zi': 3, 'durata_minute': 45,
             'descriere': '15 min banda, chest press 3x12, lat pulldown 3x12, shoulder press 3x12, cable row 3x12. Pauza 30s.',
             'tag': 'Circuit, Forta', 'img_url': 'https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=tBzbv4KcJRU'},
            {'titlu': 'Circuit Complet in Parc', 'locatie': 'aer_liber', 'obiectiv': 'slabit', 'zi': 3, 'durata_minute': 35,
             'descriere': 'Alergare 400m, 20 genuflexiuni, 15 flotari, 30s plank, 10 burpees. 4 runde. Pauza 1 min intre runde.',
             'tag': 'Circuit, Cardio', 'img_url': 'https://images.unsplash.com/photo-1476480862126-209bfaa8edc8?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=CBWQGb4LyAM'},
            # Ziua 4 - Zi de Recuperare Activa
            {'titlu': 'Stretching si Yoga Light', 'locatie': 'acasa', 'obiectiv': 'slabit', 'zi': 4, 'durata_minute': 30,
             'descriere': 'Yoga flow usor: cat-cow, downward dog, child pose, pigeon pose, supine twist. Focus pe respiratie si recuperare.',
             'tag': 'Recuperare, Flexibilitate', 'img_url': 'https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=v7AYKMP6rOE'},
            {'titlu': 'Cardio Usor + Stretching', 'locatie': 'sala', 'obiectiv': 'slabit', 'zi': 4, 'durata_minute': 30,
             'descriere': '15 min bicicleta la intensitate joasa, apoi 15 min stretching complet. Recuperare activa.',
             'tag': 'Recuperare, Cardio', 'img_url': 'https://images.unsplash.com/photo-1574680096145-d05b474e2155?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=v7AYKMP6rOE'},
            {'titlu': 'Plimbare Lunga 60 Minute', 'locatie': 'aer_liber', 'obiectiv': 'slabit', 'zi': 4, 'durata_minute': 60,
             'descriere': 'Plimbare in pas alert prin natura. Permite recuperarea musculara si arde calorii fara stres articular.',
             'tag': 'Recuperare, Cardio', 'img_url': 'https://images.unsplash.com/photo-1551698618-1dfe5d97d256?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=CBWQGb4LyAM'},
            # Ziua 5 - Tabata Intens
            {'titlu': 'Tabata 16 Minute Intens', 'locatie': 'acasa', 'obiectiv': 'slabit', 'zi': 5, 'durata_minute': 20,
             'descriere': '8 runde: 20s efort maxim, 10s pauza. Exercitii: burpees, sprint pe loc, squat jumps, plank jacks. 4 blocuri.',
             'tag': 'HIIT, Tabata', 'img_url': 'https://images.unsplash.com/photo-1517836357463-d25dfeac3438?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=ml6cT4AZdqI'},
            {'titlu': 'Full Body Circuit Sala', 'locatie': 'sala', 'obiectiv': 'slabit', 'zi': 5, 'durata_minute': 45,
             'descriere': 'Leg press, chest press, lat pulldown, cable row, shoulder press, leg curl. 3 runde x 12 rep. Pauza 20s intre exercitii.',
             'tag': 'Circuit, Forta', 'img_url': 'https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=tBzbv4KcJRU'},
            {'titlu': 'Alergare Tempo 5K', 'locatie': 'aer_liber', 'obiectiv': 'slabit', 'zi': 5, 'durata_minute': 30,
             'descriere': 'Alergare la ritm sustinut (tempo run). Incalzire 5 min, 20 min alergare confortabil-grea, racire 5 min.',
             'tag': 'Cardio', 'img_url': 'https://images.unsplash.com/photo-1476480862126-209bfaa8edc8?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=CBWQGb4LyAM'},
            # Ziua 6 - Total Body Tonifiere
            {'titlu': 'Total Body Tonifiere', 'locatie': 'acasa', 'obiectiv': 'slabit', 'zi': 6, 'durata_minute': 35,
             'descriere': 'Squats 4x15, lunges 3x12, push-ups 4x12, tricep dips 3x12, plank 3x60s, crunch 3x20. Circuit complet.',
             'tag': 'Tonifiere, Circuit', 'img_url': 'https://images.unsplash.com/photo-1571019614242-c5c5dee9f50b?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=UItWltVZZmE'},
            {'titlu': 'Split Upper/Lower Sala', 'locatie': 'sala', 'obiectiv': 'slabit', 'zi': 6, 'durata_minute': 50,
             'descriere': 'Squat 3x12, bench press 3x12, barbell row 3x12, shoulder press 3x12, leg extension 3x15. 10 min cardio final.',
             'tag': 'Forta, Circuit', 'img_url': 'https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=tBzbv4KcJRU'},
            {'titlu': 'Sprint si Calisthenics', 'locatie': 'aer_liber', 'obiectiv': 'slabit', 'zi': 6, 'durata_minute': 35,
             'descriere': 'Sprint 100m, 10 flotari, sprint 100m, 15 squats, sprint 100m, 30s plank. 5 runde. Pauza 90s intre runde.',
             'tag': 'HIIT, Calisthenics', 'img_url': 'https://images.unsplash.com/photo-1476480862126-209bfaa8edc8?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=CBWQGb4LyAM'},
            # Ziua 7 - Recuperare
            {'titlu': 'Yoga Restaurativa', 'locatie': 'acasa', 'obiectiv': 'slabit', 'zi': 7, 'durata_minute': 30,
             'descriere': 'Posturi de yoga restaurativa: child pose, legs up the wall, reclined butterfly, savasana. Focus pe relaxare profunda.',
             'tag': 'Recuperare, Yoga', 'img_url': 'https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=v7AYKMP6rOE'},
            {'titlu': 'Inot sau Sauna', 'locatie': 'sala', 'obiectiv': 'slabit', 'zi': 7, 'durata_minute': 30,
             'descriere': '20 min inot liber la intensitate joasa sau 15 min sauna + dus rece. Recuperare prin termoterapie.',
             'tag': 'Recuperare', 'img_url': 'https://images.unsplash.com/photo-1574680096145-d05b474e2155?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=v7AYKMP6rOE'},
            {'titlu': 'Plimbare in Natura', 'locatie': 'aer_liber', 'obiectiv': 'slabit', 'zi': 7, 'durata_minute': 45,
             'descriere': 'Plimbare relaxanta in parc sau padure. Fara ritm fortat. Beneficii mentale si fizice prin contactul cu natura.',
             'tag': 'Recuperare', 'img_url': 'https://images.unsplash.com/photo-1551698618-1dfe5d97d256?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=CBWQGb4LyAM'},

            # ========== MENTINERE - 7 ZILE ==========
            # Ziua 1 - Push (Piept, Umeri, Triceps)
            {'titlu': 'Push Day Acasa', 'locatie': 'acasa', 'obiectiv': 'mentinere', 'zi': 1, 'durata_minute': 35,
             'descriere': 'Flotari 4x15, pike push-ups 3x10, diamond push-ups 3x12, dips pe scaun 3x15, plank shoulder taps 3x20.',
             'tag': 'Forta, Push', 'img_url': 'https://images.unsplash.com/photo-1598971639058-fab3c3109a00?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=UItWltVZZmE'},
            {'titlu': 'Push Day Sala', 'locatie': 'sala', 'obiectiv': 'mentinere', 'zi': 1, 'durata_minute': 50,
             'descriere': 'Bench press 4x10, incline dumbbell press 3x12, shoulder press 4x10, lateral raises 3x15, tricep pushdown 3x12.',
             'tag': 'Hipertrofie, Push', 'img_url': 'https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=tBzbv4KcJRU'},
            {'titlu': 'Calisthenics Push Parc', 'locatie': 'aer_liber', 'obiectiv': 'mentinere', 'zi': 1, 'durata_minute': 40,
             'descriere': 'Flotari variate pe banca 4x15, dips la bare 4x10, handstand hold la perete 3x20s, pike push-ups 3x10.',
             'tag': 'Calisthenics, Push', 'img_url': 'https://images.unsplash.com/photo-1476480862126-209bfaa8edc8?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=UItWltVZZmE'},
            # Ziua 2 - Pull (Spate, Biceps)
            {'titlu': 'Pull Day Acasa', 'locatie': 'acasa', 'obiectiv': 'mentinere', 'zi': 2, 'durata_minute': 35,
             'descriere': 'Superman 4x15, reverse snow angels 3x12, doorframe rows 4x12, bicep curls cu sticle apa 3x15, face pulls banda.',
             'tag': 'Forta, Pull', 'img_url': 'https://images.unsplash.com/photo-1571019614242-c5c5dee9f50b?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=UItWltVZZmE'},
            {'titlu': 'Pull Day Sala', 'locatie': 'sala', 'obiectiv': 'mentinere', 'zi': 2, 'durata_minute': 50,
             'descriere': 'Lat pulldown 4x10, barbell row 4x10, seated cable row 3x12, face pulls 3x15, barbell curl 3x12, hammer curls 3x12.',
             'tag': 'Hipertrofie, Pull', 'img_url': 'https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=EotSw18oR9w'},
            {'titlu': 'Tractiuni si Rowing Parc', 'locatie': 'aer_liber', 'obiectiv': 'mentinere', 'zi': 2, 'durata_minute': 40,
             'descriere': 'Tractiuni 5x max, Australian pull-ups 4x12, bodyweight bicep curls la bara joasa 3x15.',
             'tag': 'Calisthenics, Pull', 'img_url': 'https://images.unsplash.com/photo-1476480862126-209bfaa8edc8?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=UItWltVZZmE'},
            # Ziua 3 - Legs
            {'titlu': 'Leg Day Acasa', 'locatie': 'acasa', 'obiectiv': 'mentinere', 'zi': 3, 'durata_minute': 35,
             'descriere': 'Squats 4x20, lunges 3x15, glute bridges 4x20, calf raises 4x25, wall sit 3x45s, step-ups pe scaun 3x12.',
             'tag': 'Forta, Picioare', 'img_url': 'https://images.unsplash.com/photo-1571019614242-c5c5dee9f50b?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=UItWltVZZmE'},
            {'titlu': 'Leg Day Sala', 'locatie': 'sala', 'obiectiv': 'mentinere', 'zi': 3, 'durata_minute': 50,
             'descriere': 'Squat 4x10, leg press 3x12, Romanian deadlift 3x12, leg extension 3x15, leg curl 3x15, calf raises 4x15.',
             'tag': 'Hipertrofie, Picioare', 'img_url': 'https://images.unsplash.com/photo-1574680096145-d05b474e2155?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=tBzbv4KcJRU'},
            {'titlu': 'Alergare + Picioare Parc', 'locatie': 'aer_liber', 'obiectiv': 'mentinere', 'zi': 3, 'durata_minute': 40,
             'descriere': 'Jogging 10 min, lunges pe alee 3x20m, step-ups banca 3x15, squats 4x20, sprint scari 5x. Jogging 10 min racire.',
             'tag': 'Cardio, Picioare', 'img_url': 'https://images.unsplash.com/photo-1476480862126-209bfaa8edc8?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=CBWQGb4LyAM'},
            # Ziua 4 - Cardio + Core
            {'titlu': 'Yoga si Core', 'locatie': 'acasa', 'obiectiv': 'mentinere', 'zi': 4, 'durata_minute': 35,
             'descriere': 'Yoga flow 15 min, plank 3x60s, bicycle crunch 3x20, leg raises 3x15, russian twist 3x20, dead bug 3x12.',
             'tag': 'Core, Yoga', 'img_url': 'https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=v7AYKMP6rOE'},
            {'titlu': 'Cardio Moderat + Abs', 'locatie': 'sala', 'obiectiv': 'mentinere', 'zi': 4, 'durata_minute': 45,
             'descriere': '25 min eliptica sau bicicleta, apoi ab crunch machine 3x15, cable woodchop 3x12, plank 3x60s, hanging leg raises 3x10.',
             'tag': 'Cardio, Core', 'img_url': 'https://images.unsplash.com/photo-1574680096145-d05b474e2155?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=tBzbv4KcJRU'},
            {'titlu': 'Jogging si Stretching', 'locatie': 'aer_liber', 'obiectiv': 'mentinere', 'zi': 4, 'durata_minute': 40,
             'descriere': '25 min jogging ritm conversational, apoi 15 min stretching complet: quadriceps, hamstrings, spate, umeri.',
             'tag': 'Cardio, Flexibilitate', 'img_url': 'https://images.unsplash.com/photo-1551698618-1dfe5d97d256?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=CBWQGb4LyAM'},
            # Ziua 5 - Push (repetare)
            {'titlu': 'Upper Body Push Acasa', 'locatie': 'acasa', 'obiectiv': 'mentinere', 'zi': 5, 'durata_minute': 30,
             'descriere': 'Flotari decline 4x12, pike push-ups 3x10, dips scaun 3x15, lateral raises sticle 3x15, plank to push-up 3x10.',
             'tag': 'Forta, Push', 'img_url': 'https://images.unsplash.com/photo-1598971639058-fab3c3109a00?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=UItWltVZZmE'},
            {'titlu': 'Push Hypertrophy Sala', 'locatie': 'sala', 'obiectiv': 'mentinere', 'zi': 5, 'durata_minute': 50,
             'descriere': 'Incline bench 4x10, flat dumbbell press 3x12, cable flyes 3x15, Arnold press 3x10, tricep overhead 3x12.',
             'tag': 'Hipertrofie, Push', 'img_url': 'https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=tBzbv4KcJRU'},
            {'titlu': 'Ciclism 45 Minute', 'locatie': 'aer_liber', 'obiectiv': 'mentinere', 'zi': 5, 'durata_minute': 45,
             'descriere': 'Ciclism moderat cu intervale de efort pe pante. Ritm 18-22 km/h. Excelent cardio fara impact articular.',
             'tag': 'Cardio, Rezistenta', 'img_url': 'https://images.unsplash.com/photo-1541625602330-2277a4c46182?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=CBWQGb4LyAM'},
            # Ziua 6 - Pull + Legs
            {'titlu': 'Full Body Complet Acasa', 'locatie': 'acasa', 'obiectiv': 'mentinere', 'zi': 6, 'durata_minute': 40,
             'descriere': 'Squats 4x15, push-ups 4x12, superman 3x15, lunges 3x12, dips 3x12, plank 3x45s. Antrenament complet.',
             'tag': 'Full Body, Forta', 'img_url': 'https://images.unsplash.com/photo-1571019614242-c5c5dee9f50b?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=UItWltVZZmE'},
            {'titlu': 'Pull + Legs Sala', 'locatie': 'sala', 'obiectiv': 'mentinere', 'zi': 6, 'durata_minute': 55,
             'descriere': 'Deadlift 4x8, barbell row 3x10, pull-ups 4x max, squat 3x10, leg press 3x12, bicep curl 3x12.',
             'tag': 'Hipertrofie, Full Body', 'img_url': 'https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=EotSw18oR9w'},
            {'titlu': 'Calisthenics Complet Parc', 'locatie': 'aer_liber', 'obiectiv': 'mentinere', 'zi': 6, 'durata_minute': 45,
             'descriere': 'Tractiuni 5x max, dips 4x10, pistol squat progresii 3x8, flotari 4x15, L-sit 3x15s.',
             'tag': 'Calisthenics, Full Body', 'img_url': 'https://images.unsplash.com/photo-1476480862126-209bfaa8edc8?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=UItWltVZZmE'},
            # Ziua 7 - Recuperare
            {'titlu': 'Pilates si Mobilitate', 'locatie': 'acasa', 'obiectiv': 'mentinere', 'zi': 7, 'durata_minute': 30,
             'descriere': 'Hundred, roll-up, single leg circle, spine stretch, saw. Focus pe mobilitate si controlul corpului.',
             'tag': 'Recuperare, Pilates', 'img_url': 'https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=v7AYKMP6rOE'},
            {'titlu': 'Inot Relaxant', 'locatie': 'sala', 'obiectiv': 'mentinere', 'zi': 7, 'durata_minute': 30,
             'descriere': '20-30 min inot liber la intensitate scazuta. Excelent pentru recuperare, mobilitate si relaxare musculara.',
             'tag': 'Recuperare, Cardio', 'img_url': 'https://images.unsplash.com/photo-1574680096145-d05b474e2155?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=v7AYKMP6rOE'},
            {'titlu': 'Plimbare si Meditatie', 'locatie': 'aer_liber', 'obiectiv': 'mentinere', 'zi': 7, 'durata_minute': 45,
             'descriere': '30 min plimbare in natura urmata de 15 min meditatie in parc. Recuperare mentala si fizica completa.',
             'tag': 'Recuperare, Mindfulness', 'img_url': 'https://images.unsplash.com/photo-1551698618-1dfe5d97d256?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=v7AYKMP6rOE'},

            # ========== INGRASARE (Masa Musculara) - 7 ZILE ==========
            # Ziua 1 - Piept si Triceps
            {'titlu': 'Piept Acasa Volum', 'locatie': 'acasa', 'obiectiv': 'ingrasare', 'zi': 1, 'durata_minute': 40,
             'descriere': 'Flotari 5x max, wide push-ups 4x15, diamond push-ups 4x12, decline push-ups 4x12, dips pe scaun 4x15.',
             'tag': 'Hipertrofie, Piept', 'img_url': 'https://images.unsplash.com/photo-1598971639058-fab3c3109a00?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=UItWltVZZmE'},
            {'titlu': 'Piept si Triceps Sala', 'locatie': 'sala', 'obiectiv': 'ingrasare', 'zi': 1, 'durata_minute': 60,
             'descriere': 'Bench press 5x5, incline dumbbell press 4x10, cable flyes 3x12, dips 4x10, tricep pushdown 4x12, skull crushers 3x12.',
             'tag': 'Hipertrofie, Forta', 'img_url': 'https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=tBzbv4KcJRU'},
            {'titlu': 'Calisthenics Push Greu', 'locatie': 'aer_liber', 'obiectiv': 'ingrasare', 'zi': 1, 'durata_minute': 45,
             'descriere': 'Dips grele 5x8 (cu rucsac), flotari archer 4x8, pseudo planche push-ups 3x8, pike push-ups elevate 4x10.',
             'tag': 'Calisthenics, Forta', 'img_url': 'https://images.unsplash.com/photo-1476480862126-209bfaa8edc8?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=UItWltVZZmE'},
            # Ziua 2 - Spate si Biceps
            {'titlu': 'Spate Acasa cu Banda', 'locatie': 'acasa', 'obiectiv': 'ingrasare', 'zi': 2, 'durata_minute': 40,
             'descriere': 'Rows cu banda elastica 5x15, superman hold 4x30s, reverse flyes 4x12, curls cu banda 4x15, chin-up negatives 3x5.',
             'tag': 'Hipertrofie, Spate', 'img_url': 'https://images.unsplash.com/photo-1571019614242-c5c5dee9f50b?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=UItWltVZZmE'},
            {'titlu': 'Spate si Biceps Masa', 'locatie': 'sala', 'obiectiv': 'ingrasare', 'zi': 2, 'durata_minute': 60,
             'descriere': 'Deadlift 5x5, barbell row 4x8, lat pulldown 4x10, seated cable row 3x12, barbell curl 4x10, hammer curls 3x12.',
             'tag': 'Hipertrofie, Forta', 'img_url': 'https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=EotSw18oR9w'},
            {'titlu': 'Tractiuni Grele Parc', 'locatie': 'aer_liber', 'obiectiv': 'ingrasare', 'zi': 2, 'durata_minute': 45,
             'descriere': 'Tractiuni cu greutate (rucsac) 5x5, wide grip pull-ups 4x8, chin-ups 4x8, bodyweight rows 3x12.',
             'tag': 'Calisthenics, Forta', 'img_url': 'https://images.unsplash.com/photo-1476480862126-209bfaa8edc8?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=UItWltVZZmE'},
            # Ziua 3 - Picioare Grele
            {'titlu': 'Picioare Acasa Volum', 'locatie': 'acasa', 'obiectiv': 'ingrasare', 'zi': 3, 'durata_minute': 40,
             'descriere': 'Bulgarian split squat 4x12, pistol squat progresii 3x8, glute bridges cu greutate 4x20, calf raises 5x25, wall sit 3x60s.',
             'tag': 'Hipertrofie, Picioare', 'img_url': 'https://images.unsplash.com/photo-1571019614242-c5c5dee9f50b?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=UItWltVZZmE'},
            {'titlu': 'Leg Day Forta Maxima', 'locatie': 'sala', 'obiectiv': 'ingrasare', 'zi': 3, 'durata_minute': 60,
             'descriere': 'Back squat 5x5, leg press 4x12, Romanian deadlift 4x10, leg extension 3x15, leg curl 3x15, calf raises 4x20.',
             'tag': 'Hipertrofie, Forta', 'img_url': 'https://images.unsplash.com/photo-1574680096145-d05b474e2155?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=tBzbv4KcJRU'},
            {'titlu': 'Sprint si Sarituri', 'locatie': 'aer_liber', 'obiectiv': 'ingrasare', 'zi': 3, 'durata_minute': 35,
             'descriere': 'Sprint 60m x 8, box jumps pe banca 4x10, squat jumps 4x12, lunges pe alee 3x20m. Pauza 2 min intre seturi.',
             'tag': 'Putere, Sprint', 'img_url': 'https://images.unsplash.com/photo-1476480862126-209bfaa8edc8?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=CBWQGb4LyAM'},
            # Ziua 4 - Umeri si Brate
            {'titlu': 'Umeri si Brate Acasa', 'locatie': 'acasa', 'obiectiv': 'ingrasare', 'zi': 4, 'durata_minute': 35,
             'descriere': 'Pike push-ups 4x12, lateral raises sticle 4x15, front raises 3x12, curls cu sticle 4x15, dips 4x15.',
             'tag': 'Hipertrofie, Brate', 'img_url': 'https://images.unsplash.com/photo-1598971639058-fab3c3109a00?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=UItWltVZZmE'},
            {'titlu': 'Umeri si Brate Sala', 'locatie': 'sala', 'obiectiv': 'ingrasare', 'zi': 4, 'durata_minute': 55,
             'descriere': 'Military press 5x5, lateral raises 4x12, face pulls 3x15, barbell curl 4x10, hammer curls 3x12, tricep overhead 3x12.',
             'tag': 'Hipertrofie, Forta', 'img_url': 'https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=EotSw18oR9w'},
            {'titlu': 'Handstand si Brate Parc', 'locatie': 'aer_liber', 'obiectiv': 'ingrasare', 'zi': 4, 'durata_minute': 40,
             'descriere': 'Handstand hold la perete 5x30s, pike push-ups elevate 4x10, chin-ups 4x8, dips 4x10.',
             'tag': 'Calisthenics, Forta', 'img_url': 'https://images.unsplash.com/photo-1476480862126-209bfaa8edc8?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=UItWltVZZmE'},
            # Ziua 5 - Piept si Spate (superset)
            {'titlu': 'Push-Pull Superset Acasa', 'locatie': 'acasa', 'obiectiv': 'ingrasare', 'zi': 5, 'durata_minute': 40,
             'descriere': 'Superset: flotari 4x15 + superman 4x15, dips 3x12 + banda rows 3x12, plank 3x45s + reverse plank 3x30s.',
             'tag': 'Hipertrofie, Superset', 'img_url': 'https://images.unsplash.com/photo-1571019614242-c5c5dee9f50b?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=UItWltVZZmE'},
            {'titlu': 'Piept si Spate Superset Sala', 'locatie': 'sala', 'obiectiv': 'ingrasare', 'zi': 5, 'durata_minute': 60,
             'descriere': 'Superset: bench press 4x8 + barbell row 4x8, incline press 3x10 + lat pulldown 3x10, cable fly 3x12 + cable row 3x12.',
             'tag': 'Hipertrofie, Superset', 'img_url': 'https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=tBzbv4KcJRU'},
            {'titlu': 'Muscle-Up Training', 'locatie': 'aer_liber', 'obiectiv': 'ingrasare', 'zi': 5, 'durata_minute': 45,
             'descriere': 'Muscle-up progresii 5x3, explosive pull-ups 4x5, dips grele 4x8, flotari clapping 3x8.',
             'tag': 'Calisthenics, Putere', 'img_url': 'https://images.unsplash.com/photo-1476480862126-209bfaa8edc8?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=UItWltVZZmE'},
            # Ziua 6 - Picioare si Core
            {'titlu': 'Picioare si Core Acasa', 'locatie': 'acasa', 'obiectiv': 'ingrasare', 'zi': 6, 'durata_minute': 40,
             'descriere': 'Squats cu salt 4x12, lunges 4x12, single leg deadlift 3x10, plank 3x60s, ab wheel 3x10, russian twist 3x20.',
             'tag': 'Hipertrofie, Core', 'img_url': 'https://images.unsplash.com/photo-1571019614242-c5c5dee9f50b?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=UItWltVZZmE'},
            {'titlu': 'Picioare Volum + Abs Sala', 'locatie': 'sala', 'obiectiv': 'ingrasare', 'zi': 6, 'durata_minute': 60,
             'descriere': 'Front squat 4x8, hack squat 3x12, walking lunges 3x20, hip thrust 4x12, hanging leg raises 3x12, cable crunch 3x15.',
             'tag': 'Hipertrofie, Forta', 'img_url': 'https://images.unsplash.com/photo-1574680096145-d05b474e2155?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=tBzbv4KcJRU'},
            {'titlu': 'Strongman Outdoor', 'locatie': 'aer_liber', 'obiectiv': 'ingrasare', 'zi': 6, 'durata_minute': 45,
             'descriere': 'Farmer walks 4x40m, bear crawls 4x20m, sandbag carries 4x30m, sprint 4x60m. Antrenament functional de forta bruta.',
             'tag': 'Forta, Functional', 'img_url': 'https://images.unsplash.com/photo-1476480862126-209bfaa8edc8?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=CBWQGb4LyAM'},
            # Ziua 7 - Recuperare
            {'titlu': 'Stretching si Foam Rolling', 'locatie': 'acasa', 'obiectiv': 'ingrasare', 'zi': 7, 'durata_minute': 30,
             'descriere': 'Foam rolling complet 15 min (spate, picioare, glute), apoi stretching static 15 min. Esential pentru recuperare musculara.',
             'tag': 'Recuperare, Mobilitate', 'img_url': 'https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=v7AYKMP6rOE'},
            {'titlu': 'Sauna si Inot Usor', 'locatie': 'sala', 'obiectiv': 'ingrasare', 'zi': 7, 'durata_minute': 40,
             'descriere': '15 min sauna, dus rece, 20 min inot usor. Promoveaza recuperarea prin termoterapie si miscare cu impact zero.',
             'tag': 'Recuperare', 'img_url': 'https://images.unsplash.com/photo-1574680096145-d05b474e2155?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=v7AYKMP6rOE'},
            {'titlu': 'Plimbare si Mobilitate', 'locatie': 'aer_liber', 'obiectiv': 'ingrasare', 'zi': 7, 'durata_minute': 45,
             'descriere': '30 min plimbare relaxanta, apoi 15 min mobilitate articulara: cercuri umeri, deschideri sold, rotiri trunchi.',
             'tag': 'Recuperare, Mobilitate', 'img_url': 'https://images.unsplash.com/photo-1551698618-1dfe5d97d256?w=400&h=250&fit=crop',
             'youtube_url': 'https://www.youtube.com/watch?v=v7AYKMP6rOE'},
        ]
        for e in exercitii:
            Exercitiu.objects.create(**e)
        self.stdout.write(self.style.SUCCESS(f'Exercitii index: {Exercitiu.objects.count()}'))

    def _seed_program_zilnic(self):
        self.stdout.write('--- Program zilnic ---')
        ProgramZilnic.objects.all().delete()
        programe = [
            # ========== SLABIT ==========
            {'tip_dieta': 'slabit', 'zi': 1, 'trezire': '06:30', 'mic_dejun_ora': '07:00', 'gustare1_ora': '10:00',
             'antrenament_ora': '10:30', 'antrenament_tip': 'HIIT Full Body', 'pranz_ora': '12:30', 'gustare2_ora': '15:30',
             'cina_ora': '19:00', 'relaxare_ora': '21:00', 'somn_ora': '22:30', 'ore_somn': 8,
             'sfat_somn': 'Evita ecranele cu 1h inainte de culcare. Citeste o carte sau mediteaza 10 min.',
             'sfat_zi': 'Bea minim 2.5L apa. Antrenamentul HIIT dimineata accelereaza metabolismul pentru toata ziua.'},
            {'tip_dieta': 'slabit', 'zi': 2, 'trezire': '06:30', 'mic_dejun_ora': '07:00', 'gustare1_ora': '10:00',
             'antrenament_ora': '11:00', 'antrenament_tip': 'Picioare si Core', 'pranz_ora': '12:30', 'gustare2_ora': '15:30',
             'cina_ora': '19:00', 'relaxare_ora': '21:00', 'somn_ora': '22:30', 'ore_somn': 8,
             'sfat_somn': 'Camera trebuie sa fie racuroasa (18-20°C) si complet intunecata pentru somn optim.',
             'sfat_zi': 'Focus pe proteine la fiecare masa. Proteinele mentin masa musculara in deficit caloric.'},
            {'tip_dieta': 'slabit', 'zi': 3, 'trezire': '06:30', 'mic_dejun_ora': '07:00', 'gustare1_ora': '10:00',
             'antrenament_ora': '10:30', 'antrenament_tip': 'Upper Body + Cardio', 'pranz_ora': '12:30', 'gustare2_ora': '15:30',
             'cina_ora': '19:00', 'relaxare_ora': '21:00', 'somn_ora': '22:30', 'ore_somn': 8,
             'sfat_somn': 'Magneziu (400mg) inainte de culcare ajuta la relaxare musculara si somn mai profund.',
             'sfat_zi': 'Mananca incet si mesteca bine. Satierea vine dupa 20 de minute.'},
            {'tip_dieta': 'slabit', 'zi': 4, 'trezire': '07:00', 'mic_dejun_ora': '07:30', 'gustare1_ora': '10:00',
             'antrenament_ora': '10:00', 'antrenament_tip': 'Recuperare Activa (Yoga/Plimbare)', 'pranz_ora': '12:30', 'gustare2_ora': '15:30',
             'cina_ora': '19:00', 'relaxare_ora': '21:00', 'somn_ora': '22:30', 'ore_somn': 8.5,
             'sfat_somn': 'Zi de recuperare = mai mult somn. Corpul se repara in timpul somnului profund.',
             'sfat_zi': 'Zi de recuperare activa. Nu sari peste ea! Recuperarea previne accidentarile si burnout-ul.'},
            {'tip_dieta': 'slabit', 'zi': 5, 'trezire': '06:30', 'mic_dejun_ora': '07:00', 'gustare1_ora': '10:00',
             'antrenament_ora': '10:30', 'antrenament_tip': 'Tabata Intens', 'pranz_ora': '12:30', 'gustare2_ora': '15:30',
             'cina_ora': '19:00', 'relaxare_ora': '21:00', 'somn_ora': '22:30', 'ore_somn': 8,
             'sfat_somn': 'Rutina de seara constanta: ceai de musetel, stretching usor, respiratie 4-7-8.',
             'sfat_zi': 'Tabata e scurt dar intens. Nu manca cu 1.5h inainte. Hidrateaza-te bine dupa.'},
            {'tip_dieta': 'slabit', 'zi': 6, 'trezire': '06:30', 'mic_dejun_ora': '07:00', 'gustare1_ora': '10:00',
             'antrenament_ora': '10:30', 'antrenament_tip': 'Total Body Tonifiere', 'pranz_ora': '12:30', 'gustare2_ora': '15:30',
             'cina_ora': '19:00', 'relaxare_ora': '21:00', 'somn_ora': '22:30', 'ore_somn': 8,
             'sfat_somn': 'Evita cafeaua dupa ora 14:00. Cofeina ramane in organism 6-8 ore.',
             'sfat_zi': 'Ultimul antrenament intens al saptamanii. Da totul! Maine e zi de odihna.'},
            {'tip_dieta': 'slabit', 'zi': 7, 'trezire': '08:00', 'mic_dejun_ora': '08:30', 'gustare1_ora': '11:00',
             'antrenament_ora': '11:00', 'antrenament_tip': 'Recuperare (Yoga/Plimbare)', 'pranz_ora': '13:00', 'gustare2_ora': '16:00',
             'cina_ora': '19:00', 'relaxare_ora': '21:00', 'somn_ora': '22:30', 'ore_somn': 9,
             'sfat_somn': 'Profita de duminica pentru somn mai lung. 9 ore de somn ajuta la recuperare completa.',
             'sfat_zi': 'Zi libera! Plimbare, yoga, timp cu familia. Pregateste meal prep pentru saptamana urmatoare.'},

            # ========== MENTINERE ==========
            {'tip_dieta': 'mentinere', 'zi': 1, 'trezire': '06:30', 'mic_dejun_ora': '07:00', 'gustare1_ora': '10:00',
             'antrenament_ora': '17:00', 'antrenament_tip': 'Push Day (Piept, Umeri, Triceps)', 'pranz_ora': '12:30', 'gustare2_ora': '15:00',
             'cina_ora': '19:30', 'relaxare_ora': '21:30', 'somn_ora': '23:00', 'ore_somn': 7.5,
             'sfat_somn': 'Mentine un program de somn constant, chiar si in weekend. Ritmul circadian e crucial.',
             'sfat_zi': 'Push day: focus pe piept si umeri. Mananca o gustare cu carbohidrati inainte de antrenament.'},
            {'tip_dieta': 'mentinere', 'zi': 2, 'trezire': '06:30', 'mic_dejun_ora': '07:00', 'gustare1_ora': '10:00',
             'antrenament_ora': '17:00', 'antrenament_tip': 'Pull Day (Spate, Biceps)', 'pranz_ora': '12:30', 'gustare2_ora': '15:00',
             'cina_ora': '19:30', 'relaxare_ora': '21:30', 'somn_ora': '23:00', 'ore_somn': 7.5,
             'sfat_somn': 'Citeste 20 min inainte de somn. Reduce stresul si imbunatateste calitatea somnului.',
             'sfat_zi': 'Pull day: spate si biceps. Concentreaza-te pe contractia musculara, nu pe greutate.'},
            {'tip_dieta': 'mentinere', 'zi': 3, 'trezire': '06:30', 'mic_dejun_ora': '07:00', 'gustare1_ora': '10:00',
             'antrenament_ora': '17:00', 'antrenament_tip': 'Leg Day', 'pranz_ora': '12:30', 'gustare2_ora': '15:00',
             'cina_ora': '19:30', 'relaxare_ora': '21:30', 'somn_ora': '23:00', 'ore_somn': 8,
             'sfat_somn': 'Dupa leg day, somnul e extra important. Muschii picioarelor au nevoie de 48-72h recuperare.',
             'sfat_zi': 'Leg day e cel mai greu dar si cel mai important. Nu sari peste el niciodata!'},
            {'tip_dieta': 'mentinere', 'zi': 4, 'trezire': '06:30', 'mic_dejun_ora': '07:00', 'gustare1_ora': '10:00',
             'antrenament_ora': '17:00', 'antrenament_tip': 'Cardio + Core', 'pranz_ora': '12:30', 'gustare2_ora': '15:00',
             'cina_ora': '19:30', 'relaxare_ora': '21:30', 'somn_ora': '23:00', 'ore_somn': 7.5,
             'sfat_somn': 'Evita mesele grele cu 3h inainte de culcare. Un ceai de musetel e perfect.',
             'sfat_zi': 'Zi de cardio moderat si core. Ajuta la recuperare si mentine sanatatea cardiovasculara.'},
            {'tip_dieta': 'mentinere', 'zi': 5, 'trezire': '06:30', 'mic_dejun_ora': '07:00', 'gustare1_ora': '10:00',
             'antrenament_ora': '17:00', 'antrenament_tip': 'Push Day 2', 'pranz_ora': '12:30', 'gustare2_ora': '15:00',
             'cina_ora': '19:30', 'relaxare_ora': '21:30', 'somn_ora': '23:00', 'ore_somn': 7.5,
             'sfat_somn': 'Daca ai probleme cu somnul, incearca tehnica 4-7-8: inspira 4s, tine 7s, expira 8s.',
             'sfat_zi': 'Al doilea push day. Variaza exercitiile fata de Ziua 1 pentru stimulare diferita.'},
            {'tip_dieta': 'mentinere', 'zi': 6, 'trezire': '06:30', 'mic_dejun_ora': '07:00', 'gustare1_ora': '10:00',
             'antrenament_ora': '17:00', 'antrenament_tip': 'Pull + Legs', 'pranz_ora': '12:30', 'gustare2_ora': '15:00',
             'cina_ora': '19:30', 'relaxare_ora': '21:30', 'somn_ora': '23:00', 'ore_somn': 8,
             'sfat_somn': 'Foloseste masca de somn si dopuri de urechi daca ai vecini zgomotosi sau lumina stradala.',
             'sfat_zi': 'Antrenament complet astazi. Mananca bine dupa - corpul are nevoie de nutrienti pentru refacere.'},
            {'tip_dieta': 'mentinere', 'zi': 7, 'trezire': '08:00', 'mic_dejun_ora': '09:00', 'gustare1_ora': '11:30',
             'antrenament_ora': '11:00', 'antrenament_tip': 'Recuperare (Pilates/Plimbare)', 'pranz_ora': '13:00', 'gustare2_ora': '16:00',
             'cina_ora': '19:00', 'relaxare_ora': '21:00', 'somn_ora': '22:30', 'ore_somn': 8.5,
             'sfat_somn': 'Duminica seara, pregateste-te mental pentru saptamana. Mediteaza 10 min si mergi la culcare devreme.',
             'sfat_zi': 'Zi de odihna si recuperare. Fa meal prep, planifica antrenamentele si relaxeaza-te.'},

            # ========== INGRASARE (Masa Musculara) ==========
            {'tip_dieta': 'ingrasare', 'zi': 1, 'trezire': '06:00', 'mic_dejun_ora': '06:30', 'gustare1_ora': '09:30',
             'antrenament_ora': '16:30', 'antrenament_tip': 'Piept si Triceps', 'pranz_ora': '12:00', 'gustare2_ora': '15:00',
             'cina_ora': '19:30', 'relaxare_ora': '21:30', 'somn_ora': '22:30', 'ore_somn': 7.5,
             'sfat_somn': 'Hormonul de crestere se elibereaza in primele ore de somn profund. Culca-te devreme!',
             'sfat_zi': 'Piept si triceps azi. Mananca un shake proteic + carbohidrati in max 30 min dupa antrenament.'},
            {'tip_dieta': 'ingrasare', 'zi': 2, 'trezire': '06:00', 'mic_dejun_ora': '06:30', 'gustare1_ora': '09:30',
             'antrenament_ora': '16:30', 'antrenament_tip': 'Spate si Biceps', 'pranz_ora': '12:00', 'gustare2_ora': '15:00',
             'cina_ora': '19:30', 'relaxare_ora': '21:30', 'somn_ora': '22:30', 'ore_somn': 7.5,
             'sfat_somn': 'Caseina (proteina lenta) inainte de culcare ajuta la sinteza proteica peste noapte.',
             'sfat_zi': 'Spate si biceps. Deadlift e rege! Foloseste centura si incalzeste-te bine.'},
            {'tip_dieta': 'ingrasare', 'zi': 3, 'trezire': '06:00', 'mic_dejun_ora': '06:30', 'gustare1_ora': '09:30',
             'antrenament_ora': '16:30', 'antrenament_tip': 'Picioare Grele', 'pranz_ora': '12:00', 'gustare2_ora': '15:00',
             'cina_ora': '19:30', 'relaxare_ora': '21:30', 'somn_ora': '22:00', 'ore_somn': 8,
             'sfat_somn': 'Dupa leg day, 8h de somn sunt MINIME. Muschii cresc in somn, nu la sala.',
             'sfat_zi': 'Leg day = cel mai caloric antrenament. Mananca mai mult azi. Squatul stimuleaza tot corpul.'},
            {'tip_dieta': 'ingrasare', 'zi': 4, 'trezire': '06:00', 'mic_dejun_ora': '06:30', 'gustare1_ora': '09:30',
             'antrenament_ora': '16:30', 'antrenament_tip': 'Umeri si Brate', 'pranz_ora': '12:00', 'gustare2_ora': '15:00',
             'cina_ora': '19:30', 'relaxare_ora': '21:30', 'somn_ora': '22:30', 'ore_somn': 7.5,
             'sfat_somn': 'Temperatura optima: 18-20°C. Corpul trebuie sa scada temperatura interna pentru somn profund.',
             'sfat_zi': 'Umeri si brate. Volum mare, greutati moderate. Focus pe mind-muscle connection.'},
            {'tip_dieta': 'ingrasare', 'zi': 5, 'trezire': '06:00', 'mic_dejun_ora': '06:30', 'gustare1_ora': '09:30',
             'antrenament_ora': '16:30', 'antrenament_tip': 'Piept si Spate (Superset)', 'pranz_ora': '12:00', 'gustare2_ora': '15:00',
             'cina_ora': '19:30', 'relaxare_ora': '21:30', 'somn_ora': '22:30', 'ore_somn': 7.5,
             'sfat_somn': 'Consistenta > durata. Mai bine 7.5h in fiecare noapte decat 6h + 10h random.',
             'sfat_zi': 'Superset piept + spate = volum dublu in timp redus. Antrenament eficient si intens.'},
            {'tip_dieta': 'ingrasare', 'zi': 6, 'trezire': '06:00', 'mic_dejun_ora': '06:30', 'gustare1_ora': '09:30',
             'antrenament_ora': '16:30', 'antrenament_tip': 'Picioare si Core', 'pranz_ora': '12:00', 'gustare2_ora': '15:00',
             'cina_ora': '19:30', 'relaxare_ora': '21:30', 'somn_ora': '22:00', 'ore_somn': 8,
             'sfat_somn': 'ZMA (zinc + magneziu) seara ajuta la recuperare si somn mai profund pentru sportivi.',
             'sfat_zi': 'Al doilea leg day. Front squat si hip thrust pentru variatie. Mananca din belsug!'},
            {'tip_dieta': 'ingrasare', 'zi': 7, 'trezire': '08:00', 'mic_dejun_ora': '08:30', 'gustare1_ora': '11:00',
             'antrenament_ora': '11:00', 'antrenament_tip': 'Recuperare (Stretching/Plimbare)', 'pranz_ora': '13:00', 'gustare2_ora': '16:00',
             'cina_ora': '19:30', 'relaxare_ora': '21:00', 'somn_ora': '22:00', 'ore_somn': 9,
             'sfat_somn': 'Duminica = refacere totala. 9h de somn. Corpul sintetizeaza proteine si repara fibre musculare.',
             'sfat_zi': 'Recuperare completa. Foam rolling, stretching, meal prep. Pregateste-te mental pentru saptamana.'},
        ]
        for p in programe:
            ProgramZilnic.objects.create(**p)
        self.stdout.write(self.style.SUCCESS(f'Programe zilnice: {ProgramZilnic.objects.count()}'))
