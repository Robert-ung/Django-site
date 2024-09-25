from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pokemon_id>/', views.detail, name='detail'),  
    path('favorites/', views.favorite_list, name='favorite_list'), 
    path('<int:pokemon_id>/add_favorite/', views.add_favorite, name='add_favorite'),  
    path('<int:pokemon_id>/del_favorite/', views.del_favorite, name='del_favorite'),  
]

