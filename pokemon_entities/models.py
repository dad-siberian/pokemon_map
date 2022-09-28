from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200, null=True, blank=True)
    title_jp = models.CharField(max_length=200, null=True, blank=True)
    evolved_from = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True, related_name='evolves_into'
    )
    photo = models.ImageField(upload_to='pokemons', null=True, blank=True)
    description = models.TextField(default='')

    def __str__(self) -> str:
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    lat = models.FloatField()
    lon = models.FloatField()
    appeared_at = models.DateTimeField(default=None)
    disappeared_at = models.DateTimeField(default=None)
    level = models.IntegerField()
    health = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    stamina = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.pokemon}. {self.level} уровень'
