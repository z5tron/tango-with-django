from django.contrib import admin

from .models import Category, Page

class PageAdmin(admin.ModelAdmin):
    fields = ['title', 'category']
    list_display = ('title', 'category', 'views', 'likes')
    
admin.site.register(Category)
admin.site.register(Page, PageAdmin)

# Register your models here.
