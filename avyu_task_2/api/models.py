from django.db import models
from django.utils.translation import gettext_lazy


class Card(models.model):
    '''Модель карты'''
    class CardStatuses(models.TetxChoices):
        '''Возможные статусы карты'''
        ACTIVE = 'AC', gettext_lazy('Active')
        INACTIVE = 'IA', gettext_lazy('Inactive')
        EXPIRED = 'EX', gettext_lazy('Expired')

    series = models.IntegerField()
    number = models.IntegerField()
    date_release = models.DateTimeField()
    date_expiration = models.DateTimeField()
    status = models.CharField(
        max_length=2,
        choices=CardStatuses.choices,
        default=CardStatuses.INACTIVE
    )
