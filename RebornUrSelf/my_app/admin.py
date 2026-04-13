from django.contrib import admin
from .models import (
    UserProfile, Diet, Recipe, Workout, MealImage,
    VipPayment, DailyLog, ChatMessage, WeightEntry,
    Citat, Reteta, Exercitiu,
    ProgramZilnic, DailyCheckIn, Notification, Achievement, UserAchievement,
)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'goal', 'weight_kg', 'is_vip', 'suspected_insulin_resistance')
    list_filter = ('goal', 'is_vip')


class RecipeInline(admin.TabularInline):
    model = Recipe
    extra = 1


@admin.register(Diet)
class DietAdmin(admin.ModelAdmin):
    list_display = ('name', 'goal', 'calories_per_day', 'is_insulin_friendly')
    list_filter = ('goal',)
    inlines = [RecipeInline]


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'diet', 'day', 'meal_type', 'calories', 'image_url')
    list_filter = ('diet', 'day', 'meal_type')


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('title', 'environment', 'difficulty', 'duration_minutes', 'goal', 'image_url')
    list_filter = ('environment', 'difficulty', 'goal')


@admin.register(MealImage)
class MealImageAdmin(admin.ModelAdmin):
    list_display = ('user', 'estimated_calories', 'comment', 'created_at')


@admin.register(VipPayment)
class VipPaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount_eur', 'created_at', 'is_active')


@admin.register(DailyLog)
class DailyLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'meal_type', 'food_name', 'calories')
    list_filter = ('date', 'meal_type')
    search_fields = ('food_name',)


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'content_preview', 'created_at')
    list_filter = ('role',)

    def content_preview(self, obj):
        return obj.content[:80]
    content_preview.short_description = 'Mesaj'


@admin.register(WeightEntry)
class WeightEntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'weight', 'date')


@admin.register(Citat)
class CitatAdmin(admin.ModelAdmin):
    list_display = ('tip', 'text')


@admin.register(Reteta)
class RetetaAdmin(admin.ModelAdmin):
    list_display = ('nume', 'tip', 'masa', 'zi', 'kcal')
    list_filter = ('tip', 'masa')


@admin.register(Exercitiu)
class ExercitiuAdmin(admin.ModelAdmin):
    list_display = ('titlu', 'locatie', 'obiectiv', 'tag')
    list_filter = ('locatie', 'obiectiv')


@admin.register(ProgramZilnic)
class ProgramZilnicAdmin(admin.ModelAdmin):
    list_display = ('tip_dieta', 'zi')


@admin.register(DailyCheckIn)
class DailyCheckInAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'score')
    list_filter = ('date',)


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'type', 'is_read', 'created_at')
    list_filter = ('type', 'is_read')


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('name', 'condition_type', 'condition_value', 'color')


@admin.register(UserAchievement)
class UserAchievementAdmin(admin.ModelAdmin):
    list_display = ('user', 'achievement', 'earned_at')
