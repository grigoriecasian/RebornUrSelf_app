from django.core.management.base import BaseCommand
from my_app.models import Achievement


class Command(BaseCommand):
    help = 'Creeaza achievement-urile default'

    def handle(self, *args, **options):
        achievements = [
            {'name': 'Primul Pas', 'description': 'Primul check-in completat', 'icon': 'fa-shoe-prints', 'color': 'emerald', 'condition_type': 'checkin_streak', 'condition_value': 1},
            {'name': 'Saptamana Perfecta', 'description': '7 zile consecutive de check-in', 'icon': 'fa-fire', 'color': 'orange', 'condition_type': 'checkin_streak', 'condition_value': 7},
            {'name': 'Luna de Foc', 'description': '30 zile consecutive de check-in', 'icon': 'fa-crown', 'color': 'yellow', 'condition_type': 'checkin_streak', 'condition_value': 30},
            {'name': 'Tracker Dedicat', 'description': '10 alimente inregistrate', 'icon': 'fa-utensils', 'color': 'blue', 'condition_type': 'meals_logged', 'condition_value': 10},
            {'name': 'Nutritionist', 'description': '50 alimente inregistrate', 'icon': 'fa-bowl-food', 'color': 'purple', 'condition_type': 'meals_logged', 'condition_value': 50},
            {'name': 'Prima Cantarire', 'description': 'Prima inregistrare de greutate', 'icon': 'fa-weight-scale', 'color': 'teal', 'condition_type': 'weight_logged', 'condition_value': 1},
            {'name': 'Dedicat', 'description': '7 zile active pe platforma', 'icon': 'fa-calendar-check', 'color': 'indigo', 'condition_type': 'days_active', 'condition_value': 7},
            {'name': 'Veteran', 'description': '30 zile active pe platforma', 'icon': 'fa-medal', 'color': 'amber', 'condition_type': 'days_active', 'condition_value': 30},
            {'name': 'Scanner AI', 'description': 'Prima scanare AI a unei mese', 'icon': 'fa-camera', 'color': 'pink', 'condition_type': 'scans_done', 'condition_value': 1},
            {'name': 'Chef AI', 'description': '10 scanari AI realizate', 'icon': 'fa-wand-magic-sparkles', 'color': 'rose', 'condition_type': 'scans_done', 'condition_value': 10},
        ]

        created = 0
        for a in achievements:
            _, was_created = Achievement.objects.get_or_create(
                name=a['name'],
                defaults=a,
            )
            if was_created:
                created += 1

        self.stdout.write(self.style.SUCCESS(f'{created} achievements create, {len(achievements) - created} existente'))
