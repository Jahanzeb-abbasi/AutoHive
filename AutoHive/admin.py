from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Showroom)
admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(Engine)
admin.site.register(Feature)
admin.site.register(Car)