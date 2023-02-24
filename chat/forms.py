from django import forms
from .models import ImageSend

class ImageForm(forms.ModelForm):
    
    class Meta:
        model = ImageSend
        fields = '__all__'
