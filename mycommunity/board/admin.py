from django.contrib import admin
from .models import Board


# Register your models here.
class BoardAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'subject', 'contents', 'created_time']

admin.site.register(Board, BoardAdmin)

