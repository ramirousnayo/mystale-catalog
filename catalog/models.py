from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Creature(models.Model):

    ELEMENT_CHOICES = [
        ('fuego',   'Fuego'),
        ('agua',    'Agua'),
        ('tierra',  'Tierra'),
        ('rayo',    'Rayo'),
        ('sombra',  'Sombra'),
        ('cristal', 'Cristal'),
        ('viento',  'Viento'),
        ('hielo',   'Hielo'),
    ]

    name = models.CharField(
        max_length=120,
        unique=True,
        verbose_name='Nombre'
    )
    element = models.CharField(
        max_length=20,
        choices=ELEMENT_CHOICES,
        verbose_name='Categoría elemental'
    )
    threat_level = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        verbose_name='Nivel de amenaza'
    )
    description = models.TextField(
        verbose_name='Descripción de campo'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Criatura'
        verbose_name_plural = 'Criaturas'

    def __str__(self):
        return self.name


class CombatStats(models.Model):
    creature = models.OneToOneField(
        Creature,
        on_delete=models.CASCADE,
        related_name='combat_stats'
    )
    hp      = models.PositiveSmallIntegerField(verbose_name='HP')
    attack  = models.PositiveSmallIntegerField(verbose_name='Ataque')
    defense = models.PositiveSmallIntegerField(verbose_name='Defensa')
    speed   = models.PositiveSmallIntegerField(verbose_name='Velocidad')

    class Meta:
        verbose_name = 'Estadísticas de combate'

    def __str__(self):
        return f'Stats — {self.creature.name}'
