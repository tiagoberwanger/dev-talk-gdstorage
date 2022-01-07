from django.forms import ModelForm
from motorcycles.models import Motorcycles


# Create the form class.
class MotorcycleForm(ModelForm):
    class Meta:
        model = Motorcycles
        fields = ['motorcycle_name']


# Creating a form to add a motorcycle.
form = MotorcycleForm()