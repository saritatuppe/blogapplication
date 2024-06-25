from django.contrib import admin
from .models import post


class postAdmin(admin.ModelAdmin):
    list_display = ['id','title','contact','date_pasted','author']
    

admin.site.register(post,postAdmin)