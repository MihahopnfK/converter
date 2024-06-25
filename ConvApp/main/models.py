from django.db import models


# Create your models here.
class file_storage(models.Model):
    file = models.FileField(upload_to='stl_file')
