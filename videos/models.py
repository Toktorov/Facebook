from django.db import models
from users.models import User

# Create your models here.
class Video(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_video")
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    video_file = models.FileField(upload_to="videos/")

    def __str__(self):
        return self.title