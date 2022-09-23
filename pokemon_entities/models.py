from django.db import models  # noqa F401

class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='pokemons', null=True, blank=True)


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
