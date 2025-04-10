from django import forms
from .models import Medecin, Commentaire
from .models import Aborder, POLARITE_CHOICES, Aspect
from django.forms import ModelForm
from .models import Aborder

from django import forms
from django import forms
from .models import Medecin, Quartier

class MedecinForm(forms.ModelForm):
    quartier_nom = forms.CharField(max_length=100, required=False, label="Nom du Quartier")
    quartier_ville = forms.CharField(max_length=100, required=False, label="Ville du Quartier")
    
    class Meta:
        model = Medecin
        fields = ['nom', 'prenom', 'specialite', 'email', 'telephone', 'quartier']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Si un médecin a un quartier associé, on pré-remplit les champs
        if self.instance.quartier:
            self.fields['quartier_nom'].initial = self.instance.quartier.nom
            self.fields['quartier_ville'].initial = self.instance.quartier.ville

    def save(self, commit=True):
        # Si un quartier et une ville sont fournis, créez un nouveau quartier
        quartier_nom = self.cleaned_data.get('quartier_nom')
        quartier_ville = self.cleaned_data.get('quartier_ville')

        if quartier_nom and quartier_ville:
            quartier, created = Quartier.objects.get_or_create(nom=quartier_nom, ville=quartier_ville)
            self.instance.quartier = quartier  # Associer le médecin à ce quartier

        return super().save(commit=commit)


        
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
    def __init__(self, *args, **kwargs):
        self.commentaire = kwargs.pop('commentaire', None)
        super().__init__(*args, **kwargs)

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

        if self.commentaire and aspect:
            if Aborder.objects.filter(commentaire=self.commentaire, aspect=aspect).exists():
                raise forms.ValidationError(
                    f"L'aspect '{aspect}' a déjà été sélectionné pour ce commentaire."
                )
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