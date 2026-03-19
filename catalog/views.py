from django.shortcuts import render, get_object_or_404, redirect
from django.db import transaction
from .models import Creature
from .forms import CreatureForm, CombatStatsForm


def creature_list(request):
    element = request.GET.get('element', '')
    qs = Creature.objects.select_related('combat_stats')

    if element:
        qs = qs.filter(element=element)

    context = {
        'creatures': qs,
        'element_choices': Creature.ELEMENT_CHOICES,
        'selected_element': element,
    }
    return render(request, 'catalog/creature_list.html', context)


def creature_detail(request, pk):
    creature = get_object_or_404(
        Creature.objects.select_related('combat_stats'), pk=pk
    )
    return render(request, 'catalog/creature_detail.html', {'creature': creature})


def creature_create(request):
    if request.method == 'POST':
        form = CreatureForm(request.POST)
        stats_form = CombatStatsForm(request.POST)

        if form.is_valid() and stats_form.is_valid():
            with transaction.atomic():
                creature = form.save()
                stats = stats_form.save(commit=False)
                stats.creature = creature
                stats.save()
            return redirect('catalog:detail', pk=creature.pk)
    else:
        form = CreatureForm()
        stats_form = CombatStatsForm()

    return render(request, 'catalog/creature_form.html', {
        'form': form,
        'stats_form': stats_form,
    })
