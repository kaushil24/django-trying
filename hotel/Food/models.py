from django.db import models

# Create your models here.
class FoodBill(models.Model):
    Name_of_Guest = models.ForeignKey('guests.guest',on_delete=models.CASCADE)
    Order = models.ForeignKey('Menu', on_delete=models.CASCADE)


class Menu(models.Model):
    Item_Name = models.CharField(max_length=64)
    Item_Details = models.TextField(default=" ")
    Price = models.FloatField()
    def __str__(self):
        return '%s (₹ %s)' %(self.Item_Name,self.Price)

