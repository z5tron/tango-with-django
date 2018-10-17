from django.contrib import admin

from .models import Category, Page

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ('name', ) }
    list_display = ('name', 'slug')
    
class PageAdmin(admin.ModelAdmin):
    fields = ['title', 'category']
    list_display = ('title', 'category', 'views', 'likes')
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)

# Register your models here.
