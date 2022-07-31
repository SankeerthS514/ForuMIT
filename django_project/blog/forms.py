from django import forms
from .models import Comment, Post
from django.contrib.auth.models import User

class AddComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']
        