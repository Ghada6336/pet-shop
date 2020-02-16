from django import forms
from .models import Petshop

class PetshopForm(forms.ModelForm):
    class Meta:
        model = Petshop
        fields = ['name','age','price']
