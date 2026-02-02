from django.db import models  # noqa F401

class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name='Покемон')
    image = models.ImageField(upload_to='pokemon_images/', verbose_name='Изображение', null=True, blank=True)

    def __str__(self):
        return self.title
# your models here
