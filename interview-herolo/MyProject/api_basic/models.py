from django.db import models


class Messages(models.Model):
    subject = models.CharField(max_length=30)
    sender = models.CharField(max_length=30)
    receiver = models.CharField(max_length=30)
    message = models.TextField(max_length=100)
    read = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
