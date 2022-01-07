from django.shortcuts import render
from django.views import View

# Create your views here.

from django.http import HttpResponse

from motorcycles.forms import MotorcycleForm


class MotorcycleView(View):
    def get(self, request):
        form = MotorcycleForm()
        context = {'form': form}
        return render(request, "motorcycles.html", context)
