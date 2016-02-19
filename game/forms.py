# -*- coding:utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _
from game.models import Game


class ScheduleForm(forms.Form):
    type = forms.ChoiceField(label=_('game type'), choices=Game.GAME_TYPES)
    file = forms.FileField(label=_('file'), help_text=_('csv'))

    def clean_type(self):
        game_type = self.cleaned_data['type']
        if game_type != 1 and Game.objects.exclude(game_type=1).exclude(status=2).exists():
            raise forms.ValidationError(_('there are unfinished games'))
        return game_type

    def save(self):
        game_type = self.cleaned_data['type']
        csv_file = self.cleaned_data['file']
        for line in csv_file.readlines():
            teams = line.strip().split(',')
            Game.create(teams, game_type=game_type)