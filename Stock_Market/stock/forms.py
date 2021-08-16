from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import widgets
from rest_framework import fields
from .models import Product,Busy_product
from django import forms
class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'email':'Email'}


class ProductAddForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['name',
            'brand',
            'price',
            'catagory',
            'rate',
            'status',
            'discription']
class Order_stock(forms.ModelForm):
    class Meta:
        model=Busy_product
        fields=['quantity']