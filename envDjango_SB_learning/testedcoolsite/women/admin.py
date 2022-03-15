from django.contrib import admin

from .models import *


class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}


# search_fields - не забывать запятую!
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


# строчка регистрации,
# первым делом класс который регистрируем,
# затем класс прописанный выше с настройками АдмПан
admin.site.register(Women, WomenAdmin)
admin.site.register(Category, CategoryAdmin)
