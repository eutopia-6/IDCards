from django.contrib import admin
from .models import idcard
# Register your models here.

class iDCardsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)

admin.site.register(idcard, iDCardsAdmin)

