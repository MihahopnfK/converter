from django.db import models

# Create your models here.
class storage (models.Model):
    title = models.CharField('название', max_length = 50)
    annons = models.CharField(max_length = 50)
    full_text = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title