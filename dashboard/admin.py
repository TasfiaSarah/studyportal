from django.contrib import admin
from . models import *
# Register your models here.
admin.site.register(Notes) #admin e notes er table dekhabe jeta models e class declare kora
admin.site.register(Homework)
admin.site.register(Todo)


#superuser, username-admin,pass-1234