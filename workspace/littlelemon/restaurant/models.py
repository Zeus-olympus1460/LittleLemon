from django.db import models

# Create your models here.
class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(default=1)
    booking_date = models.DateField()
    
    def __str__(self):
        return f" Booking for {self.name} on {self.booking_date} for {self.no_of_guests} guests"


class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(default=0)

    def __str__(self):
        return self.title + " - $" + str(self.price) + " - " + str(self.inventory) + " left in stock"