from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(Colour)
admin.site.register(State)
admin.site.register(Car)
admin.site.register(Driver)
admin.site.register(Client)
admin.site.register(Status)
admin.site.register(Order)
admin.site.register(Operator)