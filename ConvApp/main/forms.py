from django import forms
from django.core.validators import FileExtensionValidator
from .models import file_storage

class file_storageForm(forms.ModelForm):
    file = forms.FileField(validators=[FileExtensionValidator(allowed_extensions=['stl'])])
    class Meta:
        model = file_storage
        fields = ('file',)