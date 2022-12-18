from django.contrib import admin

from . import models

EMPTY = '-пусто-'


@admin.register(models.Card)
class CardAdmin(admin.ModelAdmin):
    list_display = (
    # fields = (
        'id',
        'series',
        'number',
        'date_release',
        'date_expiration',
        'status'
    )
    readonly_fields = ('id', )
    empty_value_display = EMPTY
