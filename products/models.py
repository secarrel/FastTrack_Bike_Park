from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name
    
class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    difficulty = models.CharField(max_length=20)
    capacity = models.PositiveSmallIntegerField()
    requirements = models.TextField()
    details = models.TextField()
    timeslot = models.ForeignKey('Timeslot', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
    
class Timeslot(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    available_capacity = models.PositiveSmallIntegerField()