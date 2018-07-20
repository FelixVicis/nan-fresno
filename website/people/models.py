import uuid
from django.db import models
from datetime import datetime


def upload_location(instance, filename):
    extension = filename.split('.')[-1]

    return "media/{}/{}.{}".format(instance.id, instance.id, extension)


class People(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    lastName = models.CharField(max_length=200)
    firstName = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    county = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    circumstance = models.TextField()
    age = models.CharField(max_length=4, null=True, blank=True)
    sex = models.CharField(max_length=20, null=True, blank=True)
    race = models.CharField(max_length=100, null=True, blank=True)
    eye_color = models.CharField(max_length=200, null=True, blank=True)
    hair_color = models.CharField(max_length=200, null=True, blank=True)
    weight = models.CharField(max_length=200, null=True, blank=True)
    height = models.CharField(max_length=200, null=True, blank=True)
    photo = models.ImageField(upload_to=upload_location)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return'%s %s' % (self.firstName, self.lastName)

    class Meta:
        verbose_name_plural = "Missing People"
