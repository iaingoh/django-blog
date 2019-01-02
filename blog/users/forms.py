from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    # Class meta gives us a nested namespace for configurations and keeps the configurations in one place and in the configurations, we're saying that the affected model will be the user model, so for example, when we do a form dot save, it's going to save it to this user model. The fields that we have here are the fields in the form and in what order. Now we have a completed form that inherits from the user creation form that adds that email field.
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
