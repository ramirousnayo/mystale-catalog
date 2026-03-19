from django.contrib import admin
from .models import Creature, CombatStats


class CombatStatsInline(admin.StackedInline):
    model = CombatStats
    extra = 1


@admin.register(Creature)
class CreatureAdmin(admin.ModelAdmin):
    list_display  = ['name', 'element', 'threat_level', 'created_at']
    list_filter   = ['element']
    search_fields = ['name']
    inlines       = [CombatStatsInline]
