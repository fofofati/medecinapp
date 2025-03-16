from django import forms
from .models import Medecin, Commentaire,Aspect


from django import forms
from .models import Medecin, Commentaire

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
     
