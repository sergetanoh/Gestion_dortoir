from django.shortcuts import render
from .models import Etudiant ,Batiment

# Create your views here.

def home(request): # parametre request obligatoire qui va permettre les requettes http
    liste_etudiants = Etudiant.objects.all() # tu recupere tout les objets de la classe article pour mettre dans list_article
    context = {
        "liste_etudiants": liste_etudiants
    }

    return render(request,"index.html",context)# veut dire tu m'envoi un templates appellé index.html
    # je vais dans mon dossier charo pour creer un dossier templates
    # render permet de rendre le fichier html au user et tu vas le rendre avec context



def search(request):
    #GET={"article":"cafe"} c'est ce qui ce passe dans la ligne juste apres
    query=request.GET["article"]
    liste_etudiant=Etudiant.objects.filter(nom__icontains=query) # tu vas selectioner tout les objets dont le titre est egale à qruery
    return render(request,"search.html",{"liste_etudiants":liste_etudiant})
    # les ypes de requettes : SELECT *FROM Article where titre LIKE %'query'% veut dit que si il ya des mot dans la demande de l'utilisateur et que notre titre est dedans on envoi la requettes



