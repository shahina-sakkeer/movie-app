from django.db import models

# Create your models here.

class Movies(models.Model):
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    year=models.CharField(max_length=200)
    genre=models.CharField(max_length=200)
    image=models.ImageField(upload_to="gallery")


    def __str__(self):
        return self.name
