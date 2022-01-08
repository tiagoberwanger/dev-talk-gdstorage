from django import forms


# Create the form class.
class MotorcycleForm(forms.Form):
    motorcycle_name = forms.CharField()
    motorcycle_brand = forms.CharField()


class MotorcycleImageForm(forms.Form):
    motorcycle_image = forms.FileField()
