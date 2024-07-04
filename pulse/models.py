from django.db import models
from accounts.models import CustomUser
from django.utils import timezone

class Pulse(models.Model):
    title = models.CharField(max_length=60)
    artist = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='uploaded_pulses')
    description = models.CharField(max_length=500, blank=True)
    tags = models.CharField(max_length=500, blank=True)
    duration = models.IntegerField(default=10)
    release_date = models.DateField(default=timezone.now)
    video = models.FileField(upload_to='video/pulse/')
    views = models.ManyToManyField(CustomUser, related_name='viewed_pulses', blank=True)
    likes = models.ManyToManyField(CustomUser, related_name='liked_pulses', blank=True)

    def __str__(self):
        return self.title

    def add_like(self, user):
        if user not in self.likes.all():
            self.likes.add(user)
            user.like_number += 1  # Assuming you have a like_number field on CustomUser
            user.save()
            return True
        return False

    def remove_like(self, user):
        if user in self.likes.all():
            self.likes.remove(user)
            user.like_number -= 1  # Assuming you have a like_number field on CustomUser
            user.save()
            return True
        return False

    def add_view(self, user):
        if user not in self.views.all():
            self.views.add(user)

    @property
    def like_count(self):
        return self.likes.count()

    @property
    def view_count(self):
        return self.views.count()
