from django.db import models

# Create your models here.
class FoodBill(models.Model):
    Name_of_Guest = models.ForeignKey('guests.guest',on_delete=models.CASCADE)
    Order = models.ForeignKey('Menu', on_delete=models.CASCADE)
    Quantity= models.IntegerField()
    # Order_1 = models.ForeignKey('Menu', on_delete=models.CASCADE,)
    # Quantity_1 = models.IntegerField()
    # Order_2 = models.ForeignKey('Menu', on_delete=models.CASCADE)
    # Quantity_2 = models.IntegerField()
    # Order_3 = models.ForeignKey('Menu', on_delete=models.CASCADE)
    # Quantity_3 = models.IntegerField()
    # Order_4 = models.ForeignKey('Menu', on_delete=models.CASCADE)
    # Quantity_4 = models.IntegerField()
    # Order_5 = models.ForeignKey('Menu', on_delete=models.CASCADE)
    # Quantity_5 = models.IntegerField()
    # Order_6 = models.ForeignKey('Menu', on_delete=models.CASCADE)
    # Quantity_6 = models.IntegerField()
    # Order_7 = models.ForeignKey('Menu', on_delete=models.CASCADE)
    # Quantity_7 = models.IntegerField()
    # Order_8 = models.ForeignKey('Menu', on_delete=models.CASCADE)
    # Quantity_8 = models.IntegerField()
    # Order_9 = models.ForeignKey('Menu', on_delete=models.CASCADE)
    # Quantity_9 = models.IntegerField()
    # Order_10 = models.ForeignKey('Menu', on_delete=models.CASCADE)
    # Quantity_10 = models.IntegerField()
    # Order_11 = models.ForeignKey('Menu', on_delete=models.CASCADE)
    # Quantity_11 = models.IntegerField()
    # Order_12 = models.ForeignKey('Menu', on_delete=models.CASCADE)
    # Quantity_12 = models.IntegerField()

class Menu(models.Model):
    Item_Name = models.CharField(max_length=64)
    Item_Details = models.TextField(default=" ")
    Price = models.FloatField()
    def __str__(self):
        return '%s (₹ %s)' %(self.Item_Name,self.Price)

