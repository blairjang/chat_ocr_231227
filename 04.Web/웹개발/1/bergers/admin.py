from django.contrib import admin
from bergers.models import Berger

# Register your models here.
@admin.register(Berger)
class BergerAdmin(admin.ModelAdmin):
    pass