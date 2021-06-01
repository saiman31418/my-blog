from django.contrib import admin

# Register your models here.
from .models import register1, post

admin.site.register(register1)
admin.site.register(post)
