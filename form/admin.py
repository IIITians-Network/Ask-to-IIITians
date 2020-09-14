from django.contrib import admin
from .models import Form
@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    list_display = ('query','email','institute')
    list_filter = ('institute',)
   