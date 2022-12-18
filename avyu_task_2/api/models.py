from random import randint

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy


class CustomUser(AbstractUser):
    '''Модель пользователя'''


def random_card_number():
    return str(randint(1, (10**13 - 1))).zfill(13)


class Card(models.Model):
    '''Модель карты'''
    class CardStatuses(models.TextChoices):
        '''Возможные статусы карты'''
        ACTIVE = 'AC', gettext_lazy('Active')
        INACTIVE = 'IA', gettext_lazy('Inactive')
        EXPIRED = 'EX', gettext_lazy('Expired')

    series = models.CharField(
        max_length=6,
        blank=False,
        null=False,
    )
    number = models.CharField(
        max_length=13,
        editable=False,
        default=random_card_number,
    )
    date_release = models.DateTimeField(auto_now_add=True)
    date_expiration = models.DateTimeField(
        blank=False,
        null=False,
    )
    status = models.CharField(
        max_length=2,
        choices=CardStatuses.choices,
        default=CardStatuses.INACTIVE,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['series', 'number'], name='unique_card_series_number'
            )
        ]

    # def save(self, *args, **kwargs):
    #     created = not self.pk
    #     super().save(*args, **kwargs)
    #     if created:
    #         self.number = str(randint(1, (10**14 - 1))).zfill(13)


class Purchase(models.Model):
    '''Модель покупки'''

    card = models.OneToOneField(
        Card,
        on_delete=models.CASCADE,
    )
    price = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)
