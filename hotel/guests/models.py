from django.db import models

class Guest(models.Model):
    Name =  models.CharField(max_length=120)
    EmailID = models.EmailField()
    MobileNumber = models.BigIntegerField()
    CheckIn = models.DateField()
    CheckOut = models.DateField()
    RoomCategory =  models.ForeignKey('rooms.RoomType',on_delete=models.CASCADE)
    Number_Of_Rooms  = models.IntegerField()
    Photo_ID = models.ImageField(upload_to='documents/%Y/%d/%m/')
    def __str__(self):
        return self.Name
'''
    

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
'''
'''     
        if(TypeofRooms ==1):
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
