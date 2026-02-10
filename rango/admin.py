from django.contrib import admin
from rango.models import Category, Page, UserProfile

# Register your models here.


class CategoryAdmin(admin.ModelAdmin): # type: ignore
    # make it so only the name is editable
    fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


class PageAdmin(admin.ModelAdmin): # type: ignore
    list_display = ['title', 'category', 'url']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)

