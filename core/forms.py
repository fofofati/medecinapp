from django import forms
from .models import Medecin, Commentaire
from .models import Aborder, POLARITE_CHOICES, Aspect
from django.forms import ModelForm
from .models import Aborder


class MedecinForm(forms.ModelForm):
    class Meta:
        model = Medecin
        fields = ['nom', 'prenom', 'specialite', 'email', 'telephone']

class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['contenu']


class CustomLoginForm(forms.Form):
    username = forms.CharField(
        label="Nom d'utilisateur",
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "Nom d'utilisateur"
        })
    )
    password = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': "Mot de passe"
        })
    )


class CustomLoginForm(forms.Form):
     username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': "Username"
    }))
     password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': "Password"
    }))
     

class CustomLoginForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=150)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)


class CommentFileUploadForm(forms.Form):
     file = forms.FileField(
        label="Fichier CSV ou Excel",
        widget=forms.ClearableFileInput(attrs={
            "accept": ".csv, .xlsx"  # Permet de filtrer côté navigateur
        })
    )

class DoctorFileUploadForm(forms.Form):
    file = forms.FileField(
        label="Fichier CSV ou Excel",
        widget=forms.ClearableFileInput(attrs={
            "accept": ".csv, .xlsx"
        })
    )
     
class AborderForm(forms.ModelForm):
    class Meta:
        model = Aborder
        fields = ['aspect', 'polarite']
        widgets = {
            'aspect': forms.Select(attrs={'class': 'form-control aspect-select'}),
            'polarite': forms.Select(attrs={'class': 'form-control'}),
        }
    def clean(self):
        cleaned_data = super().clean()
        aspect = cleaned_data.get('aspect')
        polarite = cleaned_data.get('polarite')

        # Vérifie si cet aspect existe déjà, indépendamment de la polarité
        if Aborder.objects.filter(aspect=aspect).exists():
            raise forms.ValidationError(f"L'aspect '{aspect}' a déjà été sélectionné et ne peut pas être ajouté à nouveau.")

        return cleaned_data 

class AspectForm(forms.ModelForm):
    class Meta:
        model = Aspect
        fields = ['nom_aspect']
        widgets = {
            'nom_aspect': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Nom du nouvel aspect'
            }),
        }