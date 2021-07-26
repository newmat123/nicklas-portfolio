from django import forms
from .models import imgs

class ImgForm(forms.ModelForm):

    title = forms.CharField(required=False)
    img = forms.ImageField(required=False)


    class Meta:
        model = imgs
        fields = ['title', 'img']