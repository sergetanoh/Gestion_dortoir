from django.urls import path
from .views import *

urlpatterns=[
    path('',dashboard,name='dashboard'),
    path('Etudiant',user_article,name='my-article'),
    path('ajouter-etudiant',Add_Etudiant.as_view(),name='ajout-article'),
    path('modifier-article/<int:pk>',update_article.as_view(),name='modif'),
    path('suprimer-article/<int:pk>',delete_article.as_view(),name='delete'),

]