from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.forms import User

from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class SearchForm(forms.Form):
    search_value = forms.CharField(max_length=200, required=False)

class FilterForm(forms.Form):
    min_price = forms.IntegerField(required=False)
    max_price = forms.Intemin_price = forms.IntegerField(required=False)
    min_tasks = forms.Intemin_price = forms.IntegerField(required=False)
    max_tasks = forms.Intemin_price = forms.IntegerField(required=False)
    category = forms.CharField(max_length=200, required=False)
    is_urgent = forms.BooleanField(required=False)

# class LoginUserForm():
#     class Meta:
#         model = User
        # fields = ['username', 'password']

