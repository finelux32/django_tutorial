from django.contrib import admin
from .models import CommunityUser


# Register your models here.
class CommunityUserAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'user_password', 'created_datetime', 'user_email']

admin.site.register(CommunityUser, CommunityUserAdmin)







