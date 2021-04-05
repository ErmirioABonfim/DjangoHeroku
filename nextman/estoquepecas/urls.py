
from django.urls import path
from .views import hello, fNome, fNome2



urlpatterns = [
    path('', hello),
    path('<str:nome>/',fNome),
    path('nome/<str:nome2>/',fNome2)
]
