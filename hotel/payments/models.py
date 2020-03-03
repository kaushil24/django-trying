from django.db import models

# Create your models here.
class Income(models.Model):
    GuestName = models.ForeignKey('guests.Guest', on_delete=models.CASCADE)
    Amount = models.DecimalField(max_digits=15, decimal_places=2)

class Expense(models.Model):
    Name = models.CharField(max_length = 32)
    Amount = models.DecimalField(max_digits=15, decimal_places=2)
    Bill_Details = models.TextField()
    Bill_Photo = models.ImageField(upload_to="bills/%d%m%y")