from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from motorcycles.forms import MotorcycleForm
from motorcycles.models import Motorcycle


def index(request):
    return render(request, "home.html")


class MotorcycleView(View):
    def get(self, request):
        form = MotorcycleForm()
        return render(request, 'motorcycles.html', {'form': form})

    def post(self, request):
        form = MotorcycleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('favorites')
        else:
            form = MotorcycleForm()
        return render(request, 'motorcycles.html', {'form': form})


class FavoritesView(View):
    def get(self, request):
        list_all_motorcycles = Motorcycle.objects.all()
        return render(request, 'favorites.html', {'motorcycles': list_all_motorcycles})
