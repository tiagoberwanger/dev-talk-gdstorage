from django.forms import ModelForm
from motorcycles.models import Motorcycle

# Create the form class.
class MotorcycleForm(ModelForm):
    class Meta:
        model = Motorcycle
        fields = ['motorcycle_name', 'motorcycle_brand', 'motorcycle_image']
        labels = {
            'motorcycle_name': ('Digite o nome da sua motocicleta'),
            'motorcycle_brand': ('Digite a marca da sua motocicleta'),
            'motorcycle_image': ('Escolha a imagem'),
        }
# Creating a form to add an article.
form = MotorcycleForm()