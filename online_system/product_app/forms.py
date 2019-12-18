from django import forms
from product_app.models import Product

class ProductList(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price',]
