from django.contrib import admin
from django.utils.html import format_html
from .models import Pokemon, PokemonEntity

@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'show_image')
    list_display_links = ('title',)
    search_fields = ('title',)
    readonly_fields = ('show_image',)
    fields = ('title', 'image', 'show_image')

    def show_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />', obj.image.url)
        return "Нет изображения"

    show_image.short_description = 'Изображение'

@admin.register(PokemonEntity)
class PokemonEntityAdmin(admin.ModelAdmin):
    list_display = ('id', 'pokemon', 'lat', 'lon', 'appeared_at', 'disappeared_at')
    list_display_links = ('pokemon',)
    list_filter = ('pokemon', 'appeared_at', 'disappeared_at')
    search_fields = ('pokemon__title',)


    fieldsets = (
        (None, {
            'fields': ('pokemon',)
        }),
        ('Координаты', {
            'fields': ('lat', 'lon'),
            'classes': ('wide',)
        }),
        ('Время', {
            'fields': ('appeared_at', 'disappeared_at'),
            'classes': ('wide',)
        }),
    )