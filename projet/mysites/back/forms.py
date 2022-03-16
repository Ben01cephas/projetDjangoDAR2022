from array import array
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,PasswordChangeForm
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *

class CustomUserCreationForm(UserCreationForm,forms.Form):
    is_fromEsmt= forms.BooleanField(required=False,label="Etudiant de L'ESMT",widget=forms.CheckboxInput(attrs={'type': 'checkbox'}))
    
    telephone = forms.CharField(
        required=True,
        max_length=50,
        strip=True,
        min_length=2,
        widget=forms.TextInput(
            attrs={
                'type':'text',
                'placeholder':'Telephone',
                'class':'peer h-10 placeholder-transparent border-b-2 bg-transparent focus:outline-none border-white/50 focus:text-[#B95252] dark:focus:text-slate-500 dark:focus:border-slate-500 focus:border-[#B95252]',
            }
        )
    )

    last_name = forms.CharField(
        label="Nom",
        required=True,
        max_length=50,
        strip=True,
        min_length=2,
        widget=forms.TextInput(
            attrs={
                'type':'text',
                'placeholder':'Nom',
                'class':'peer h-10 placeholder-transparent border-b-2 bg-transparent focus:outline-none border-white/50 focus:text-[#B95252] dark:focus:text-slate-500 dark:focus:border-slate-500 focus:border-[#B95252]',
            }
        )
    )

    first_name = forms.CharField(
        label="Prenom",
        required=True,
        max_length=50,
        strip=True,
        min_length=2,
        widget=forms.TextInput(
            attrs={
                'type':'text',
                'placeholder':'Prenom',
                'class':'peer h-10 placeholder-transparent border-b-2 bg-transparent focus:outline-none border-white/50 focus:text-[#B95252] dark:focus:text-slate-500 dark:focus:border-slate-500 focus:border-[#B95252]',
                
            }
        )
    )

    adresse = forms.CharField(
        required=True,
        max_length=50,
        strip=True,
        min_length=2,
        widget=forms.TextInput(
            attrs={
                'type':'text',
                'placeholder':'Adresse',
                'class':'peer h-10 placeholder-transparent border-b-2 bg-transparent focus:outline-none border-white/50 focus:text-[#B95252] dark:focus:text-slate-500 dark:focus:border-slate-500 focus:border-[#B95252]',
            }
        )
    )

    email = forms.CharField(
        required=True,
        max_length=50,
        strip=True,
        min_length=2,
        widget=forms.TextInput(
            attrs={
                'type':'email',
                'placeholder':'Email',
                'class':'peer h-10 placeholder-transparent border-b-2 bg-transparent focus:outline-none border-white/50 focus:text-[#B95252] dark:focus:text-slate-500 dark:focus:border-slate-500 focus:border-[#B95252]',
            }
        )
    )

    class Meta:
        model = User
        fields = ('first_name','last_name', 'telephone', 'email','adresse','is_fromEsmt')


class CustomUserChangeForm(UserChangeForm,forms.Form):
    is_fromEsmt= forms.BooleanField(required=False,label="Etudiant de L'ESMT",widget=forms.CheckboxInput(attrs={'type': 'checkbox'}))
    
    telephone = forms.CharField(
        required=True,
        max_length=50,
        strip=True,
        min_length=2,
        widget=forms.TextInput(
            attrs={
                'type':'text'
            }
        )
    )

    last_name = forms.CharField(
        label="Nom",
        required=True,
        max_length=50,
        strip=True,
        min_length=2,
        widget=forms.TextInput(
            attrs={
                'type':'text'
            }
        )
    )

    first_name = forms.CharField(
        label="Prenom",
        required=True,
        max_length=50,
        strip=True,
        min_length=2,
        widget=forms.TextInput(
            attrs={
                'type':'text'
            }
        )
    )

    adresse = forms.CharField(
        required=True,
        max_length=50,
        strip=True,
        min_length=2,
        widget=forms.TextInput(
            attrs={
                'type':'text'
            }
        )
    )
    
    class Meta:
        model = User
        fields = ('first_name','last_name', 'telephone', 'adresse','is_fromEsmt')
        
class passwordChangeForm(PasswordChangeForm,forms.Form):
    class Meta:
        model=User
        fields = ()

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

class contactForm(forms.Form):
    email = forms.EmailField(
        required=True,
        max_length=50,
        min_length=2,
        widget=forms.EmailInput(
            attrs={
                'type':'email'
            }
        )
    )

    message = forms.CharField(
        required=True,
        widget=forms.Textarea
    )

profList: array = []
filliereList: array = []

for mag in Professeur.objects.all():
    element = (mag.nom_prof, mag.nom_prof)
    profList.append(element)

for mag in Filliere.objects.all():
    element = (mag.nom_filliere, mag.nom_filliere)
    filliereList.append(element)

class EpreuveForm(forms.Form):
    nom_epreuve = forms.CharField(
        required=True,
        max_length=50,
        strip=True,
        min_length=2,
        widget=forms.TextInput(
            attrs={
                'type':'text'
            }
        )
    )

    niveau_epreuve = forms.CharField(
        required=True,
        max_length=50,
        strip=True,
        min_length=2,
        widget=forms.TextInput(
            attrs={
                'type':'text'
            }
        )
    )

    matiere = forms.CharField(
        required=True,
        max_length=50,
        strip=True,
        min_length=2,
        widget=forms.TextInput(
            attrs={
                'type':'text'
            }
        )
    )

    annee = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                'type':'number'
            }
        )
    )

    nom_du_professeur = forms.ChoiceField(
        required=True,
        choices=[(x, y) for (x, y) in profList],
        widget=forms.Select(
            attrs={
                'type':'select'
            }
        )
    )

    filliere = forms.ChoiceField(
        required=True,
        choices=[(x, y) for (x, y) in filliereList],
        widget=forms.Select(
            attrs={
                'type':'select'
            }
        )
    )

    fichier_epreuve= forms.FileField()

    fichier_correction= forms.FileField(
        required=False
    )