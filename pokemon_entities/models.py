from django.db import models  # noqa F401

class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    title_en = models.CharField(
        max_length=200,
        verbose_name='Английское название',
        blank=True,  # может быть пустым
        default=''  # значение по умолчанию
    )
    title_jp = models.CharField(
        max_length=200,
        verbose_name='Японское название',
        blank=True,
        default=''
    )
    image = models.ImageField(upload_to='pokemon_images/', verbose_name='Изображение', null=True, blank=True)
    description = models.TextField(verbose_name='Описание', blank=True, default='')

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
        null=True,
        blank=True
    )
    disappeared_at = models.DateTimeField(
        verbose_name='Время исчезновения',
        null=True,
        blank=True
    )

    level = models.IntegerField(
        verbose_name='Уровень',
        null=True,
        blank=True
    )
    health = models.IntegerField(
        verbose_name='Здоровье',
        null=True,
        blank=True
    )
    attack = models.IntegerField(
        verbose_name='Атака',
        null=True,
        blank=True
    )
    defense = models.IntegerField(
        verbose_name='Защита',
        null=True,
        blank=True
    )
    stamina = models.IntegerField(
        verbose_name='Выносливость',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Покемон на карте'
        verbose_name_plural = 'Покемоны на карте'

    def __str__(self):
        return f"{self.pokemon.title} ({self.lat}, {self.lon})"