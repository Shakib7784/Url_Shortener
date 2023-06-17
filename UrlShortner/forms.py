from django import forms 

from .models import ShortLink

class ShortLinkForm(forms.ModelForm):
    
    long_url = forms.URLField(widget=forms.URLInput(attrs={"class":"form-control form-control-lg","placeholder":"give your url here"}))
    
    class Meta:
        model=ShortLink
        fields = ("long_url",)