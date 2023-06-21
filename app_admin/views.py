from django.shortcuts import render,redirect
from enregistrement.models import Etudiant,Batiment
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from enregistrement.forms import EtudiantForm
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib import messages

def dashboard(request):
    return render (request,'db.html')


def user_article(request):
    if not request.user.is_superuser: # si l'utilisateur n'est pas connecte et veut acceder a l'espace admin on refuse
        return redirect('login-blog')
    list_etudiant=Etudiant.objects.all()

    return render(request,'etudiant.html',{'list_etudiants':list_etudiant})



class Add_Etudiant(LoginRequiredMixin, CreateView):
    model = Etudiant
    form_class = EtudiantForm
    template_name = "ajout-etudiant.html"
    success_url = "Etudiant"

    def form_valid(self, form):
        form.instance.user = self.request.user

        # Vérifier le nombre d'étudiants dans la chambre
        chambre = form.cleaned_data.get('chambre')
        print("Valeur de la chambre:", chambre)  # Ajouter un message de débogage pour vérifier la valeur
        if chambre:
            if chambre.etudiant_set.count() >= 2:
                messages.error(self.request, 'La chambre est déjà occupée par deux étudiants.')
                return self.form_invalid(form)  # Afficher les erreurs de validation
        return super().form_valid(form)


    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        # Récupérer le bâtiment sélectionné dans le formulaire
        batiment_id = self.request.POST.get('batiment')
        if batiment_id:
            batiment = Batiment.objects.get(id=batiment_id)
            form.fields['chambre'].queryset = batiment.chambre_set.all()

        return form

        
    

class update_article(LoginRequiredMixin,UpdateView):
    model=Etudiant
    form_class=EtudiantForm
    template_name="app_admin/article_form.html"

    
class delete_article(LoginRequiredMixin,DeleteView):
    model=Etudiant
    success_url='../Etudiant'
    template_name="app_admin/article_confirm_delete.html"




