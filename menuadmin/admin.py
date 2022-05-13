from django.contrib import admin
from .models import MenuItem

class MenuAdmin(admin.ModelAdmin):
	list_display = ('name', 'description', 'price')

admin.site.register(MenuItem, MenuAdmin)