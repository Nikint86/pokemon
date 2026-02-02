import folium
from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.utils.timezone import now
from .models import Pokemon, PokemonEntity


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    current_time = now()

    active_entities = PokemonEntity.objects.filter(
        appeared_at__lte=current_time,
        disappeared_at__gte=current_time
    ).select_related('pokemon')

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    for entity in active_entities:
        img_url = entity.pokemon.image.url if entity.pokemon.image else DEFAULT_IMAGE_URL
        add_pokemon(
            folium_map,
            entity.lat,
            entity.lon,
            request.build_absolute_uri(img_url)
        )

    pokemons_on_page = []
    for pokemon in Pokemon.objects.all():
        has_active_entities = pokemon.entities.filter(
            appeared_at__lte=current_time,
            disappeared_at__gte=current_time
        ).exists()

        if has_active_entities:
            img_url = pokemon.image.url if pokemon.image else DEFAULT_IMAGE_URL
            pokemons_on_page.append({
                'pokemon_id': pokemon.id,
                'img_url': request.build_absolute_uri(img_url),
                'title_ru': pokemon.title,
            })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    # Получаем покемона из базы данных
    pokemon = get_object_or_404(Pokemon, id=pokemon_id)

    current_time = now()

    active_entities = pokemon.entities.filter(
        appeared_at__lte=current_time,
        disappeared_at__gte=current_time
    )

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    for entity in active_entities:
        img_url = pokemon.image.url if pokemon.image else DEFAULT_IMAGE_URL
        add_pokemon(
            folium_map,
            entity.lat,
            entity.lon,
            request.build_absolute_uri(img_url)
        )

    pokemon_data = {
        'pokemon_id': pokemon.id,
        'title_ru': pokemon.title,
        'title_en': '',
        'title_jp': '',
        'img_url': pokemon.image.url if pokemon.image else DEFAULT_IMAGE_URL,
        'description': '',
        'entities': []
    }

    for entity in active_entities:
        pokemon_data['entities'].append({
            'level': entity.level,
            'lat': entity.lat,
            'lon': entity.lon,
            'health': entity.health,
            'attack': entity.attack,
            'defense': entity.defense,
            'stamina': entity.stamina,
            'appeared_at': entity.appeared_at,
            'disappeared_at': entity.disappeared_at,
        })

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(),
        'pokemon': pokemon_data,
    })
