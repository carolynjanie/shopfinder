from django.contrib import admin
# from .models import Shop
# Register your models here.
from shops import models as p_models

# admin.site.register("Shop")
admin.site.register(p_models.Shop)