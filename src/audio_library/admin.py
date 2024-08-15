from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.License)
class LisenceAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    list_display_links = ('user', )
    list_filter = ('user',)





@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')




@admin.register(models.Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name')
    list_display_links = ('user', )
    list_filter = ('user',)





@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'track')
    list_display_links = ('user', )



@admin.register(models.PlayList)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title')
    list_display_links = ('user', )
    search_fields = ('user',  'tracks__title')
