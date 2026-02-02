from django.db import migrations, models

def set_default_values(apps, schema_editor):
    PokemonEntity = apps.get_model('pokemon_entities', 'PokemonEntity')
    for entity in PokemonEntity.objects.all():
        if entity.level is None:
            entity.level = 1
        if entity.health is None:
            entity.health = 100
        if entity.attack is None:
            entity.attack = 10
        if entity.defense is None:
            entity.defense = 10
        if entity.stamina is None:
            entity.stamina = 100
        entity.save()

class Migration(migrations.Migration):
    dependencies = [
        ('pokemon_entities', '0005_pokemonentity_attack_pokemonentity_defense_and_more'),
    ]

    operations = [
        migrations.RunPython(set_default_values),
        migrations.AlterField(
            model_name='pokemonentity',
            name='level',
            field=models.IntegerField(verbose_name='Уровень', default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='health',
            field=models.IntegerField(verbose_name='Здоровье', default=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='attack',
            field=models.IntegerField(verbose_name='Атака', default=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='defense',
            field=models.IntegerField(verbose_name='Защита', default=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='stamina',
            field=models.IntegerField(verbose_name='Выносливость', default=100),
            preserve_default=False,
        ),
    ]