from django.db import models
from django.conf import settings
from django.dispatch import receiver

class Chat(models.Model):
    receiver_id = models.IntegerField()
    sender_id = models.IntegerField()
    file_id = models.IntegerField()
    status = models.CharField(max_length=1, choices=(
        ('A', 'Active'),
        ('D', 'Deactive'),)),
    Creator_id = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)