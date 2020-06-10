  
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    #Require email is defaulted to true and adds email
    email = forms.EmailField()

    # Nested namespace for configurate the model creation
    class Meta:
        # Model is the form we want the model to create
        model = User
        fields = ['username', 'email', 'password1', 'password2']
