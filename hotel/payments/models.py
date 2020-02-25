from django.db import models

# Create your models here.
class Payment(models.Model):
    BasePrice = models.DecimalField(max_digits=15,decimal_places=2)
    GST = models.DecimalField(max_digits=15,decimal_places=2)
    FinalPrice = models.DecimalField(max_digits=15,decimal_places=2)
    GuestName = models.ForeignKey('guests.Guest', on_delete=models.CASCADE)