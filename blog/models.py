from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    created = models.DateTimeField(default = timezone.now)
    content = RichTextField()
    image = models.ImageField(upload_to ='blog/')
    slug = models.SlugField(max_length = 200)
    tags = models.ManyToManyField(Tag, blank=True)
    title= models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.title)
        super().save(*args, **kwargs)