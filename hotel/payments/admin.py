from django.contrib import admin

# Register your models here.
from .models import Income
from .models import Expense
admin.site.register(Income)
admin.site.register(Expense)
