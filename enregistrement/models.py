from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Batiment(models.Model):
    nom = models.CharField(max_length=100)
    nombre_chambres = models.PositiveIntegerField()

    def __str__(self):
        return self.nom


class Chambre(models.Model):
    numero = models.CharField(max_length=10)
    batiment = models.ForeignKey(Batiment, on_delete=models.CASCADE)
    occupee = models.BooleanField(default=False)

    def __str__(self):
        return self.numero


class Etudiant(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    chambre = models.ForeignKey(Chambre, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.nom} {self.prenom}"

    def get_absolute_url(self):
        return reverse("Etudiant") 




"""
class Add_Etudiant(LoginRequiredMixin,CreateView):
    model = Etudiant
    form_class = EtudiantForm
    template_name = "ajout-etudiant.html"
    success_url = "my-article"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        # Récupérer le bâtiment sélectionné dans le formulaire
        batiment_id = self.request.POST.get('batiment')
        if batiment_id:
            batiment = get_object_or_404(Batiment, id=batiment_id)
            form.fields['chambre'].queryset = batiment.chambre_set.filter(etudiant__isnull=True)

        return form

    def form_valid(self, form):
        form.instance.user = self.request.user

        # Vérifier le nombre d'étudiants dans la chambre
        chambre = form.cleaned_data.get('chambre')
        if chambre:
            if chambre.etudiant_set.count() >= 2:
                form.add_error('chambre', 'La chambre est déjà occupée par deux étudiants.')

        return super().form_valid(form)"""       