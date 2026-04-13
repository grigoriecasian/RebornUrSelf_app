from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, MealImage, DailyLog, WeightEntry, DailyCheckIn


class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        label='Parola',
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Parola', 'class': 'form-input'}
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Confirma parola', 'class': 'form-input'}
        ),
        label='Confirma parola'
    )

    class Meta:
        model = User
        fields = ('username', 'email')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Nume utilizator', 'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-input'}),
        }

    def clean(self):
        cleaned = super().clean()
        p1 = cleaned.get('password')
        p2 = cleaned.get('password2')
        if p1 and p2 and p1 != p2:
            self.add_error('password2', 'Parolele nu coincid.')
        return cleaned


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('goal', 'gender', 'weight_kg', 'height_cm', 'age', 'suspected_insulin_resistance')
        labels = {
            'goal': 'Obiectiv',
            'gender': 'Gen',
            'weight_kg': 'Greutate (kg)',
            'height_cm': 'Inaltime (cm)',
            'age': 'Varsta',
            'suspected_insulin_resistance': 'Suspiciune rezistenta la insulina',
        }
        widgets = {
            'goal': forms.Select(attrs={'class': 'form-input'}),
            'gender': forms.Select(attrs={'class': 'form-input'}),
            'weight_kg': forms.NumberInput(attrs={'step': '0.1', 'placeholder': 'ex: 75.5', 'class': 'form-input'}),
            'height_cm': forms.NumberInput(attrs={'step': '0.1', 'placeholder': 'ex: 175', 'class': 'form-input'}),
            'age': forms.NumberInput(attrs={'placeholder': 'ex: 28', 'class': 'form-input'}),
        }


class MealImageForm(forms.ModelForm):
    class Meta:
        model = MealImage
        fields = ('image',)
        labels = {'image': 'Fotografie cu masa'}


class InsulinQuestionnaireForm(forms.Form):
    frequent_hunger = forms.BooleanField(
        required=False, label='Foame frecventa / pofte de dulce')
    abdominal_fat = forms.BooleanField(
        required=False, label='Grasime concentrata pe abdomen')
    tired_after_meals = forms.BooleanField(
        required=False, label='Somnolenta dupa masa')
    family_history = forms.BooleanField(
        required=False, label='Rude cu diabet sau rezistenta la insulina')
    dark_skin_patches = forms.BooleanField(
        required=False, label='Pete intunecate pe piele (acanthosis nigricans)')
    thirst = forms.BooleanField(
        required=False, label='Sete excesiva / urinare frecventa')


class AICompanionForm(forms.Form):
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 3,
            'placeholder': 'Intreaba-ma orice despre nutritie, antrenamente sau sanatate...',
            'class': 'form-input',
        }),
        label=''
    )


class DailyLogForm(forms.ModelForm):
    class Meta:
        model = DailyLog
        fields = ('date', 'meal_type', 'food_name', 'calories', 'protein', 'carbs', 'fat')
        labels = {
            'date': 'Data',
            'meal_type': 'Tipul mesei',
            'food_name': 'Aliment',
            'calories': 'Calorii (kcal)',
            'protein': 'Proteine (g)',
            'carbs': 'Carbohidrati (g)',
            'fat': 'Grasimi (g)',
        }
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-input'}),
            'meal_type': forms.Select(attrs={'class': 'form-input'}),
            'food_name': forms.TextInput(attrs={'placeholder': 'ex: Piept de pui cu orez', 'class': 'form-input'}),
            'calories': forms.NumberInput(attrs={'placeholder': '0', 'class': 'form-input'}),
            'protein': forms.NumberInput(attrs={'step': '0.1', 'placeholder': '0', 'class': 'form-input'}),
            'carbs': forms.NumberInput(attrs={'step': '0.1', 'placeholder': '0', 'class': 'form-input'}),
            'fat': forms.NumberInput(attrs={'step': '0.1', 'placeholder': '0', 'class': 'form-input'}),
        }


class WeightEntryForm(forms.ModelForm):
    class Meta:
        model = WeightEntry
        fields = ('date', 'weight', 'note')
        labels = {
            'date': 'Data',
            'weight': 'Greutate (kg)',
            'note': 'Nota (optional)',
        }
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-input'}),
            'weight': forms.NumberInput(attrs={'step': '0.1', 'placeholder': 'ex: 75.5', 'class': 'form-input'}),
            'note': forms.TextInput(attrs={'placeholder': 'ex: dupa antrenament', 'class': 'form-input'}),
        }


class DailyCheckInForm(forms.ModelForm):
    class Meta:
        model = DailyCheckIn
        fields = ('followed_diet', 'followed_workout', 'followed_sleep', 'drank_water', 'no_junk_food')
        labels = {
            'followed_diet': 'Am respectat dieta',
            'followed_workout': 'Am facut antrenamentul',
            'followed_sleep': 'Am dormit suficient',
            'drank_water': 'Am baut destula apa',
            'no_junk_food': 'Am evitat junk food',
        }
