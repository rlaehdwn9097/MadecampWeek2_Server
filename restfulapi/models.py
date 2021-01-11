from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30)
    userid = models.CharField(max_length=255, blank=True)
    number = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    @property
    def get_id(self):
        return self.id


class Photos(models.Model):
    image = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

