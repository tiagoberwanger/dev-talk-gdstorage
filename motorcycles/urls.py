from django.urls import path

from .views import MotorcycleView, FavoritesView, index

urlpatterns = [
    path('', index, name='home'),
    path('motorcycles/add', MotorcycleView.as_view(), name='motorcycles'),
    path('motorcycles/favorites', FavoritesView.as_view(), name='favorites'),
] 
