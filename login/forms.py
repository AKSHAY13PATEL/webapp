from django import forms
from .models import Document,RepoData
from django.contrib.auth.models import User


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', 'repository')

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class RepoForm(forms.ModelForm):
    class Meta:
        model=RepoData
        fields=('repo_name','description')
