from django.contrib import admin
from .models import Season, Episode, ReferenceCategory, Character, Reference


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ['number', 'year']

@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ['number', 'season', 'title', 'aired']
    list_filter = ['season']

@admin.register(ReferenceCategory)
class ReferenceCategory(admin.ModelAdmin):
    list_display = ['category']

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ['name', 'aka', 'actor']

@admin.register(Reference)
class ReferenceAdmin(admin.ModelAdmin):
    list_display = ['id', 'season', 'episode', 'category', 'title',
                    'slug', 'time', 'image', 'dialog', 'explanation', 'tags']
    list_filter = ['season', 'episode', 'characters', 'category']
    filter_horizontal = ('characters',)
