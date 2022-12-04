from django import forms
from .models import Order, OrderProduct,Payment


class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=['first_name', 'last_name', 'phone', 'email', 'address_1', 'address_1', 'town', 'state', 'order_note']