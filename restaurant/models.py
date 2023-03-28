from django.db import models

# Create your models here.
class Booking(models.Model):
    first_name = models.CharField(max_length=255)
    reservation_slot = models.SmallIntegerField(default=6)
    reservation_time = models.DateTimeField()

    def __str__(self): 
        return self.first_name    

class Menu(models.Model):
    title = models.CharField(max_length = 255)
    price = models.DecimalField(max_digits= 10, decimal_places=2,)
    inventory = models.SmallIntegerField(default=5)

    def __str__(self):
        return f'{self.title} : {str(self.price)}'
