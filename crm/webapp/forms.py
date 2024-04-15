from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Record

from django import forms
from django.forms.widgets import PasswordInput, TextInput

# User Creation[registration]
class CreateUserForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'password1', 'password2']


# User Login
class LoginForm(AuthenticationForm):
  username = forms.CharField(widget=TextInput(attrs={'class': 'custom-class', 'placeholder': 'Username'}))
  password = forms.CharField(widget=PasswordInput())


# Create Record
class AddRecordForm(forms.ModelForm):
  class Meta:
    model = Record
    fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'country','state', 'city']


# Update Record
class UpdateRecordForm(forms.ModelForm):
  class Meta:
    model = Record
    fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'country','state', 'city']