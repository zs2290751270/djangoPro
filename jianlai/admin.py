from django.contrib import admin
from .models import Wsb


class WsbManager(admin.ModelAdmin):
    list_display = [
        'id',
        'author',
        'content',
    ]


admin.site.register(Wsb, WsbManager)
