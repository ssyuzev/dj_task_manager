from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=35)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=35)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Task(models.Model):
    category = models.ForeignKey(Category, related_name='tasks')
    tag = models.ForeignKey(Tag, related_name='tasks')
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=500, blank=True, default='')
    due_date = models.DateField()
    author = models.ForeignKey(User, related_name='tasks')
    performers = models.ManyToManyField(User, related_name='performers')

    def __str__(self):
        return self.title
