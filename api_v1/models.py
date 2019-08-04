from django.contrib.auth import get_user_model
from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
import uuid
import random
UserModel = get_user_model()


class Attendee(models.Model):
    """
    Attendee Model
    Defines attributes af an attendee
    """
    first_name = models.CharField("first name", max_length=32)
    middle_name = models.CharField("middle name", max_length=64, blank=True, null=True, default=None)
    last_name = models.CharField("last name", max_length=32)
    phone_number = models.CharField("phone number", max_length=128)
    email = models.CharField("email", max_length=32)
    ticket = models.UUIDField("ticket", primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_winner = models.BooleanField(blank=True, null=True, default=False)
    class Meta:
        ordering = ('first_name', 'last_name')
    

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return "{} {} {}".format(self.first_name,
        self.middle_name if self.middle_name else '',
        self.last_name)

    @classmethod
    def ticket_picker(self):
        participants = [a.pk for a in self.objects.filter(is_winner=False)]
        winner = ''
        for i in range(0,100):
            winner = random.choice(participants)
        return winner

    def get_update_url(self):
        return reverse('dashboard:attendee-update', kwargs={'pk': self.pk})

    
    def get_delete_url(self):
        return reverse('dashboard:attendee-delete', kwargs={'pk': self.pk})