from django.contrib import admin
from basket.models import *

# Register your models here.
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display=('name','thumb' )
    search_fields=('name',)
    def thumb(self,obj):
        return mark_safe("<img src='%s' width='40' height='40'>"% obj.logo.url)
    thumb.allow_tags = True
    thumb.__name__ = 'logo'

#admin.site.register(Image, ImageAdmin)

#class TeamAdmin(admin.ModelAdmin):
#    list_display = ('name','photo')
#    search_fields = ('name',)

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name','thumb')
    search_fields = ('name','nickname','rut')
    list_filter = ('team',)
    list_filter = ('birthdate',)
    def thumb(self,obj):
        return mark_safe("<img src='%s' width='40' height='40'>"% obj.photo.url)
    thumb.allow_tags = True
    thumb.__name__ = 'photo'

@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ('name','age')

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('name','code')
