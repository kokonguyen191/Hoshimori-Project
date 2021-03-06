from django.contrib import admin
from django import forms

from hoshimori.models import *


class IrousAdminForm(forms.ModelForm):

    weak = forms.MultipleChoiceField(choices=WEAPON_CHOICES, widget=forms.CheckboxSelectMultiple())

    def clean_weak(self):
        return self.cleaned_data["weak"]

    strong = forms.MultipleChoiceField(choices=WEAPON_CHOICES, widget=forms.CheckboxSelectMultiple())

    def clean_strong(self):
        return self.cleaned_data["strong"]

    guard = forms.MultipleChoiceField(choices=WEAPON_CHOICES, widget=forms.CheckboxSelectMultiple())

    def clean_guard(self):
        return self.cleaned_data["guard"]


class IrousAdmin(admin.ModelAdmin):
    form = IrousAdminForm

class CardAdmin(admin.ModelAdmin):
    list_display = ('name', '_cache_totals_last_update','owner',)
    ordering = ('-_cache_totals_last_update','-id')

admin.site.register(Account)
admin.site.register(OwnedCard) # Will removed later
admin.site.register(Student)
admin.site.register(Card, CardAdmin)
# admin.site.register(ActionSkillEffect)
# admin.site.register(ActionSkill)
admin.site.register(Weapon)
admin.site.register(WeaponUpgrade)
# admin.site.register(WeaponEffect)
admin.site.register(Stage)
admin.site.register(StageDifficulty)
# admin.site.register(Nakayoshi)
admin.site.register(Irous, IrousAdmin)
admin.site.register(IrousVariation)
