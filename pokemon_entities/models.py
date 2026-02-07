from django.db import models

class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    title_en = models.CharField(
        max_length=200,
        verbose_name='Английское название',
        blank=True,
        null=True,
    )
    title_jp = models.CharField(
        max_length=200,
        verbose_name='Японское название',
        blank=True,
        null=True,
    )
    image = models.ImageField(upload_to='pokemon_images/', verbose_name='Изображение', null=True, blank=True)
    description = models.TextField(verbose_name='Описание', blank=True,null=True)

    previous_evolution = models.ForeignKey(
        'self',  # ссылка на самого себя
        on_delete=models.SET_NULL,  # если предка удалят, ставим NULL
        null=True,
        blank=True,
        verbose_name='Из кого эволюционировал',
        related_name='next_evolutions'
    )
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

    appeared_at = models.DateTimeField(
        verbose_name='Время появления',
    )
    disappeared_at = models.DateTimeField(
        verbose_name='Время исчезновения',
    )

    level = models.IntegerField(
        verbose_name='Уровень',
        null=True,
        blank=True,
    )
    health = models.IntegerField(
        verbose_name='Здоровье',
        null=True,
        blank=True,
    )
    attack = models.IntegerField(
        verbose_name='Атака',
        null=True,
        blank=True,
    )
    defense = models.IntegerField(
        verbose_name='Защита',
        null=True,
        blank=True,
    )
    stamina = models.IntegerField(
        verbose_name='Выносливость',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Покемон на карте'
        verbose_name_plural = 'Покемоны на карте'

    def __str__(self):
        return f"{self.pokemon.title} ({self.lat}, {self.lon})"