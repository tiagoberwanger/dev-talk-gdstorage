from django.urls import path

from .views import MotorcycleView

urlpatterns = [
    path('', MotorcycleView.as_view(), name='motorcycles'),
]
