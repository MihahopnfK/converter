from .models import storage
from django.forms import ModelForm, TextInput, DateInput,Textarea

class storageForm(ModelForm):
    class Meta:
        model = storage
        fields = ['title','annons','full_text','date']

        widgets = {
            "title": TextInput(attrs={
                'class':'form-control',
                'placeholder':'Название статьи'
            }),
            "annons": TextInput(attrs={
                'class':'form-control',
                'placeholder':'Аннонс статьи'
            }),
            "date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'дата'
            }),
            "full-text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Тексуи статьи'
            }),
        }
