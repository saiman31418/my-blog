from django import forms
from .models import *

class registerForm(forms.ModelForm):
    class Meta:
        model=register1
        fields = "__all__"
class PostForm(forms.ModelForm):
    class Meta:
        model=post
        fields="__all__"




