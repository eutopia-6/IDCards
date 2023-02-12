from django.contrib import admin
from .models import idcard, users, chat
# Register your models here.

class iDCardsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)

class userAccounts(admin.ModelAdmin):
    list_display = ('username', 'password')

class groupchat(admin.ModelAdmin):
    list_display = ('text_field', "author")

admin.site.register(idcard, iDCardsAdmin)
admin.site.register(users, userAccounts)
admin.site.register(chat, groupchat)

