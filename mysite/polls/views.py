
from .models import Pokemon
from django.shortcuts import render, get_object_or_404, redirect

def index(request):
    pok = Pokemon.objects.all()
    return render(request, 'polls/index.html', {'pok': pok})

def detail(request, pokemon_id):
    # Récupère le Pokémon avec l'ID donné ou renvoie une erreur 404 si non trouvé
    pokemon = get_object_or_404(Pokemon, pk=pokemon_id)
    return render(request, 'polls/detail.html', {'pokemon': pokemon})

def favorite_list(request):
    favorites = Pokemon.objects.filter(is_favorite=True)
    return render(request, 'polls/favorite_list.html', {'favorites': favorites})

def add_favorite(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, pk=pokemon_id)
    pokemon.is_favorite = not pokemon.is_favorite
    pokemon.save()
    return redirect('index')

def del_favorite(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, pk=pokemon_id)
    pokemon.is_favorite = not pokemon.is_favorite
    pokemon.save()
    return redirect('favorite_list')