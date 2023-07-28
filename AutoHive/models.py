from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
fs = FileSystemStorage(location=settings.MEDIA_ROOT)

# Create your models here.

class Showroom(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Staff(models.Model):
    name = models.CharField(max_length=100)
    showroom = models.ForeignKey(Showroom, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
class Brand(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(null=True)
    def __str__(self):
        return self.name

class Feature(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Model(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    image = models.ImageField()
    feature = models.ManyToManyField(Feature)
    def __str__(self):
        return self.name

class Engine(models.Model):
    number = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.number
    
class Car(models.Model):
    chasis_number = models.CharField(max_length=100, primary_key=True)
    model = models.ForeignKey(Model, on_delete=models.CASCADE, null=True)
    engine = models.OneToOneField(Engine, on_delete=models.CASCADE, null=True)
    showroom = models.ForeignKey(Showroom, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.chasis_number


