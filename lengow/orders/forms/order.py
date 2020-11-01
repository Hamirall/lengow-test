from django import forms
from orders.models import Order
from django.forms import ModelForm

class OrdersForm(forms.Form):
    marketplace = forms.CharField(label="Marketplace", max_length=100)
    id_flux = forms.IntegerField(label="Id du flux")
    order_amount = forms.FloatField(label="Montant de la commande")
