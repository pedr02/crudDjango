from django import forms
from CRUD.models import houses
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class houseForm(forms.ModelForm):
    class Meta:
        model = houses
        fields = [
            'location',
            'address',
            'area',
            'rooms',
            'bathRooms',
            'parking',
            'price',
            'image',
        ]

class userForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]