from django.forms import ModelForm
from motorcycles.models import Motorcycle

# Create the form class.
class MotorcycleForm(ModelForm):
    class Meta:
        model = Motorcycle
        fields = ['motorcycle_name', 'motorcycle_brand', 'motorcycle_image']

# Creating a form to add an article.
form = MotorcycleForm()