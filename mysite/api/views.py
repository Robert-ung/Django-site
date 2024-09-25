from django.http import JsonResponse
from polls.models import Pokemon

def pokemon_list(request):
    # Récupérer tous les Pokémon de la base de données
    pokemons = Pokemon.objects.all()
    
    # Préparer les données pour la réponse JSON
    data = list(pokemons.values('id', 'nom', 'type', 'generation', 'couleur', 'poids', 'hauteur', 'photo'))
    
    return JsonResponse(data, safe=False)
