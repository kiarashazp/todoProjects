from django import forms
from .models import Todo
from django.core.exceptions import ValidationError


class CreateTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'body']

    title = forms.CharField(widget=forms.TextInput)
    body = forms.CharField(widget=forms.TextInput)


class UpdateTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'body']

    title = forms.CharField(widget=forms.TextInput)
    body = forms.CharField(widget=forms.TextInput)


class SearchTodoForm(forms.Form):
    search = forms.CharField()
