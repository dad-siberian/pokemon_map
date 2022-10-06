from django.db import models  # noqa F401


class Pokemon(models.Model):
    """Вид покемона"""
    title = models.CharField(max_length=200, verbose_name='Название')
    title_en = models.CharField(
        max_length=200, blank=True,
        verbose_name='Название на английском')
    title_jp = models.CharField(
        max_length=200, blank=True,
        verbose_name='Название на японском')
    evolved_from = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True,
        blank=True, related_name='evolves_into',
        verbose_name='Эволюционировал из'
    )
    photo = models.ImageField(upload_to='pokemons',
                              null=True, blank=True, verbose_name='Фото')
    description = models.TextField(default='', verbose_name='Описание', blank=True)

    def __str__(self) -> str:
        return self.title


class PokemonEntity(models.Model):
    """Модель, описывающая одну особь покемона"""
    pokemon = models.ForeignKey(
        Pokemon, on_delete=models.CASCADE, verbose_name='Покемон')
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')
    appeared_at = models.DateTimeField(
        default=None, verbose_name='Дата и время появления')
    disappeared_at = models.DateTimeField(
        default=None, verbose_name='Дата и время исчезновения')
    level = models.IntegerField(verbose_name='Уровень')
    health = models.IntegerField(verbose_name='Здоровье')
    attack = models.IntegerField(verbose_name='Сила атаки')
    defense = models.IntegerField(verbose_name='Защита')
    stamina = models.IntegerField(verbose_name='Выносливость')

    def __str__(self) -> str:
        return f'{self.pokemon}. {self.level} уровень'
