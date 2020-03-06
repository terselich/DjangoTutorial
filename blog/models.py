from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here. Django provides authentication and User model

class Post(models.Model):
    title = models.CharField(max_length=100)  # char restriction 100
    content = models.TextField()  # text field
    date_posted = models.DateTimeField(default=timezone.now)  # date posted timezone default and pass the function
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # delete cascade

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
