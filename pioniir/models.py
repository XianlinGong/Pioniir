import os

from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField


class Head(models.Model):
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join("Homes", instance)
        return None

    title = models.CharField(max_length=100)
    content = HTMLField(blank=True, default="")
    image = models.ImageField(default='default/no_image.jpg', upload_to=image_upload_to)
    published = models.DateTimeField("Date published", default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['published']


class Faq(models.Model):
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join("Faq", instance)
        return None

    question = models.CharField(max_length=200)
    answer = HTMLField(blank=True, default="")
    published = models.DateTimeField("Date published", default=timezone.now)
    image = models.ImageField(default='default/no_image.jpg', upload_to=image_upload_to, max_length=255)

    def __str__(self):
        return self.question

    class Meta:
        ordering = ['-published']
