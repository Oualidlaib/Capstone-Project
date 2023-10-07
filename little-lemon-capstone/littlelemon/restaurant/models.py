from django.db import models
# from django.core.validators import MaxValueValidator
class Booking(models.Model):
  Name = models.CharField(max_length=255)
  No_of_guests = models.IntegerField()
  Booking_date = models.DateField()
  

class Menu(models.Model):
  Title = models.CharField(max_length=255)
  Price = models.DecimalField(max_digits=10, decimal_places=2)
  Inventory = models.IntegerField()
  
  
  
