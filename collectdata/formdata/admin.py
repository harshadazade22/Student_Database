from django.contrib import admin

# Register your models here.
from formdata.models import Saveform
class saveadmin(admin.ModelAdmin):
    list_display=('name','email','moblie','address')
admin.site.register(Saveform,saveadmin)