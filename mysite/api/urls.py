from django.urls import path
from . import views

urlpatterns = [
    path('pokemons/', views.pokemon_list, name='pokemon_list'),
]
