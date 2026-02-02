from django.db import models  # noqa F401

class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name='Покемон')
    image = models.ImageField(upload_to='pokemon_images/', verbose_name='Изображение', null=True, blank=True)

    class Meta:
        verbose_name = 'Покемон'
        verbose_name_plural = 'Покемоны'

    def __str__(self):
        return self.title

class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.CASCADE,
        verbose_name='Покемон',
        related_name='entities'
    )
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')

    class Meta:
        verbose_name = 'Покемон на карте'
        verbose_name_plural = 'Покемоны на карте'

    def __str__(self):
        return f"{self.pokemon.title} ({self.lat}, {self.lon})"