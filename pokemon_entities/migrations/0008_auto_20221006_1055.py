# Generated by Django 3.1.14 on 2022-10-06 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0007_auto_20221006_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='description',
            field=models.TextField(blank=True, default='', verbose_name='Описание'),
        ),
    ]
