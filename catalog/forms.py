from django import forms
from .models import Creature, CombatStats


class CreatureForm(forms.ModelForm):
    class Meta:
        model = Creature
        fields = ['name', 'element', 'threat_level', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }


class CombatStatsForm(forms.ModelForm):
    class Meta:
        model = CombatStats
        fields = ['hp', 'attack', 'defense', 'speed']
