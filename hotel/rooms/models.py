from django.db import models

# Create your models here.

'''PremK = PREMIUM_KHODIDHAR
EconK = ECONOMY_KHODIDHAR
DortK = DORTOIR_KHODIDHAR
Spec = SPECIAL
PremN = PREMIUM_NAGAO
EconN = ECONOMY_NAGAO
'''
Room_Choices = [
    ('PREMIUM_KHODIDHAR', "Premium @ Khodidhar"),
    ('ECONOMY_KHODIDHAR', "Economy @ Khodidhar"),
    ("DORTOIR_KHODIDHAR", "Dortoir @ Khodidhar"),
    ("SPECIAL" , "Special"),
    ("PREMIUM_NAGAO", "Premium @ Nagao"),
    ("ECONOMY_NAGAO", "Economy @ Nagao")
    ]
class RoomType(models.Model):

    RoomCategory = models.CharField(
        max_length=64,
        choices = Room_Choices,
        #default=PREMIUM_KHODIDHAR
)
