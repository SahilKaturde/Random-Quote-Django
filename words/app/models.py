from django.db import models

# Create your models here.
class Data(models.Model):
    author = models.CharField(max_length=255)
    quote = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='')

    def __str__(self):
        return f"{self.author} ID={self.id}"