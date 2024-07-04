from django.db import models
from accounts.models import CustomUser
from django.utils import timezone

class Pulse(models.Model):
    title = models.CharField(max_length=60)
    artist = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='uploaded_pulse')
    description = models.CharField(default="", max_length=500)
    tags = models.CharField(default="", max_length=500)
    duration = models.IntegerField(default=10)
    release_date = models.DateField(default=timezone.now)
    video = models.FileField(upload_to='video/pulse/')
    views = models.ManyToManyField(CustomUser, related_name='viewed_pulse', blank=True)
    likes = models.ManyToManyField(CustomUser, related_name='liked_pulse', blank=True)

    def __str__(self):
        return self.title
