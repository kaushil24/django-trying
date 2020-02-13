from django.db import models

# Create your models here.
class Guest(models.Model):
    Name =  models.CharField(max_length=120)
    EmailID = models.EmailField()
    MobileNumber = models.BigIntegerField()
    CheckIn = models.DateField()
    CheckOut = models.DateField()

    Room_Choices = [
    ('PREMIUM_KHODIDHAR', "Premium @ Khodidhar"),
    ('ECONOMY_KHODIDHAR', "Economy @ Khodidhar"),
    ("DORTOIR_KHODIDHAR", "Dortoir @ Khodidhar"),
    ("SPECIAL" , "Special"),
    ("PREMIUM_NAGAO", "Premium @ Nagao"),
    ("ECONOMY_NAGAO", "Economy @ Nagao")
    ]
    RoomCategory = models.CharField(
    max_length=64,
    choices = Room_Choices,
    default="PREMIUM_KHODIDHAR"
    )

    No_of_TypeRooms = [
    ('1',"1"),
    ('2',"2"),
    ('3',"3"),
    ('4',"4"),
    ('5',"5")
    ]
    TypeofRooms = models.CharField(
        max_length =64,
        choices = No_of_TypeRooms
    )
    '''if(TypeofRooms ==1):
        NumberofRooms = models.IntegerField()
        RoomCategory1 = models.CharField(
        max_length=64,
        choices = Room_Choices,
        default="PREMIUM_KHODIDHAR"
        )
    elif(TypeofRooms == 2):
        RoomCategory1 = models.CharField(
        max_length=64,
        choices = Room_Choices,
        default="PREMIUM_KHODIDHAR"
        )
        RoomCategory2 = models.CharField(
        max_length=64,
        choices = Room_Choices,
        default="PREMIUM_KHODIDHAR"
        )
        NumberofRooms = models.IntegerField()
    elif(TypeofRooms == 3):
        RoomCategory1 = models.CharField(
        max_length=64,
        choices = Room_Choices,
        default="PREMIUM_KHODIDHAR"
        )
        RoomCategory2 = models.CharField(
        max_length=64,
        choices = Room_Choices,
        default="PREMIUM_KHODIDHAR"
        )
        RoomCategory3 = models.CharField(
        max_length=64,
        choices = Room_Choices,
        default="PREMIUM_KHODIDHAR"
        )
        NumberofRooms = models.IntegerField()
    else:
        NumberofRooms = models.IntegerField()
        '''
