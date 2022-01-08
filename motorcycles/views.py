from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View

from motorcycles.forms import MotorcycleForm, MotorcycleImageForm
from motorcycles.models import Motorcycle, MotorcycleImage


def index(request):
    return render(request, "home.html")


class MotorcycleView(View):
    def get(self, request):
        form = MotorcycleForm()
        image_form = MotorcycleImageForm()
        return render(request, 'motorcycles.html', {'form': form, 'image': image_form})

    def post(self, request):
        form = MotorcycleForm(request.POST)
        image = request.FILES.getlist('image')
        if form.is_valid():
            name = form.cleaned_data['motorcycle_name']
            brand = form.cleaned_data['motorcycle_brand']
            mc = Motorcycle.objects.create(
                motorcycle_name=name,
                motorcycle_brand=brand
            )
            MotorcycleImage.objects.create(
                motorcycle_name=mc,
                motorcycle_image=image
            )
            return HttpResponseRedirect('favorites')
        return render(request, 'motorcycles.html', {'form': form})


class FavoritesView(View):
    def get(self, request):
        list_all_motorcycles = Motorcycle.objects.all()
        list_all_images = MotorcycleImage.objects.all()
        return render(request, 'favorites.html', {'motorcycles': list_all_motorcycles, 'images': list_all_images})
