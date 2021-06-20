from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog #모델명
        fields = ['title', 'writer', 'body', 'image']#모델에 있는 속성