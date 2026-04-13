from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('home/', views.home, name='home'),

    path('register/', views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(
        template_name='wellness/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile_view, name='profile'),

    path('diets/', views.diet_list, name='diet_list'),
    path('diets/<int:diet_id>/', views.diet_detail, name='diet_detail'),
    path('recipes/', views.recipe_list, name='recipe_list'),
    path('recipes/diet/<int:diet_id>/', views.recipe_list, name='recipe_list_by_diet'),
    path('workouts/', views.workout_list, name='workout_list'),
    path('workouts/<int:workout_id>/', views.workout_detail, name='workout_detail'),

    path('ai-calories/', views.ai_calories_view, name='ai_calories'),
    path('ai-companion/', views.ai_companion_view, name='ai_companion'),
    path('ai-companion/clear/', views.clear_chat, name='clear_chat'),
    path('generate-plan/', views.generate_plan_view, name='generate_plan'),

    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('dashboard/add/', views.add_food_log, name='add_food'),
    path('dashboard/delete/<int:log_id>/', views.delete_food_log, name='delete_food'),
    path('progress/', views.progress_view, name='progress'),

    path('notifications/read/<int:notif_id>/', views.mark_notification_read, name='mark_notification_read'),
    path('notifications/dismiss-all/', views.dismiss_all_notifications, name='dismiss_all_notifications'),

    path('achievements/', views.achievements_view, name='achievements'),

    path('export/', views.export_page, name='export'),
    path('export/csv/', views.export_csv, name='export_csv'),
    path('export/print/', views.export_print, name='export_print'),

    path('vip/', views.vip_subscribe, name='vip_subscribe'),
    path('insulin-info/', views.insulin_info_view, name='insulin_info'),
]
