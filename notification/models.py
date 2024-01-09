from django.db import models

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


class Notification(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.title


@receiver(post_save, sender=Notification)
def send_notification(sender, instance, **kwargs):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "notification", 
        {
            "type": "send_notification", 
            "title": instance.title,
            "message": instance.message,
        }
    )