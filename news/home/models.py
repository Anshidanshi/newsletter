from django.db import models

# Create your models here.
from django.db import models

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    subscribed = models.BooleanField(default=True,null=True,blank=True)

    def __str__(self):
        return self.email

class Newsletter(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    img = models.URLField(null=True,blank=True)
    def __str__(self):
        return self.title
