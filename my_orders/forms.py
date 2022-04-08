from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone', 'email', 'roll_number', 'date_of_birth', 'college', 'Department', 'year','referral_code','payment_mode','razor_payment_id']
