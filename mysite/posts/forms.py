from django import forms
from .models import Post
# from mysite.posts import models

class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields = '__all__'


        #만드는 순서 url -> view -> 마지막이 템플릿