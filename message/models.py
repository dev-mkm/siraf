from django.conf import settings
from django.db import models
from chat.models import Chat

class Message(models.Model):
    message = models.TextField()
    status = models.BooleanField(choices=((False, 'notRead'), (True, 'read')))
    createDate = models.DateField(auto_now=True)
    chat_id = models.ForeignKey(Chat, on_delete=models.CASCADE)
    reply_id = models.ForeignKey("self", related_name="reply", null=True, blank=True, on_delete=models.SET_NULL)
    Creator_id = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)