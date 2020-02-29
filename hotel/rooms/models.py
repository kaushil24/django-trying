from django.db import models
'''
Room_Choices = [
    (0, "Premium @ Khodidhar"),
    (1, "Economy @ Khodidhar"),
    (2, "Dortoir @ Khodidhar"),
    (3, "Special"),
    (4, "Premium @ Nagao"),
    (5, "Economy @ Nagao")
    ]

class RoomType(models.Model):

    RoomCategory = models.CharField(
        max_length=64,
        choices = Room_Choices,
        #default=PREMIUM_KHODIDHAR
)
'''
class RoomType(models.Model):
    RoomCategory = models.CharField(max_length=64)

    def __str__(self):
        return self.RoomCategory