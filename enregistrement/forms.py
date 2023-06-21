from django import forms
from .models import Etudiant, Batiment

class EtudiantForm(forms.ModelForm):
    batiment = forms.ModelChoiceField(queryset=Batiment.objects.all(), empty_label=None)

    class Meta:
        model = Etudiant
        fields = ["nom", "prenom", "batiment", "chambre"]
        labels = {"nom": "Nom", "prenom": "Prénom", "chambre": "Chambre", "batiment": "Bâtiment"}
        widgets = {
            "nom": forms.TextInput(attrs={'class': 'form-control'}),
            "prenom": forms.TextInput(attrs={'class': 'form-control'}),
            "chambre": forms.Select(attrs={'class': 'form-control'}),
            "batiment": forms.Select(attrs={'class': 'form-control'})
        }
