from django import forms
from app1.models import Product,Order


class ProductForm(forms.ModelForm):
    class Meta:
        model= Product
        fields= ['name','catogory','quantity']

class TakeOrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=['product','order_quantity']