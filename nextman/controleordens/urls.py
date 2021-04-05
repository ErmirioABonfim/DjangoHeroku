from django.urls import path
from .views import  lista_ordens,nova_ordem,update_ordem,delete_ordem



urlpatterns = [
    path('listar',lista_ordens, name='listar'),
    path('nova/',nova_ordem, name="nova_ordem"),
    path('update/<int:idCriacao>/',update_ordem, name='update_ordem'),
    path('delete/<int:idCriacao>',delete_ordem, name='delete_ordem'),
]
