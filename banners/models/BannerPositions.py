from django.db import models
from django.contrib import admin
from django.utils import timezone


class BannerPositions(models.Model):
    STATUS_CHOICES = (
        (10, 'Active'),
        (20, 'Inactive'),
        (30, 'Deleted'),
    )
    STATUS_CHOICES_ID={
        'active':10,
        'inactive':20,
        'deleted':30,
    }
    name = models.CharField(max_length=32, unique=True)
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=10)
    created_at = models.DateField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name = "Banner Type"              # singular name in sidebar and forms
        verbose_name_plural = "Banner Types"

    def __str__(self):
        return self.name
    

