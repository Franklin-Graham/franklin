from django.db import models

# Create your models here.
class Profile(models.Model):
    Name = models.CharField(max_length=100)
    profile = models.ImageField()
    def __str__(self):
        return self.Name

class Main(models.Model):
    image = models.ImageField(upload_to='picture')
