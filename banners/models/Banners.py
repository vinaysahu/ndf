from django.db import models
from django.contrib import admin
from django.utils import timezone
from .BannerPositions import BannerPositions


class Banners(models.Model):
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
    title = models.CharField(max_length=32, unique=True)
    image = models.ImageField(upload_to='images/banners/', null=True, blank=True)
    link_url = models.CharField(max_length=32, null=True, blank=True)
    btn_title = models.CharField(max_length=32, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    banner_position_id = models.ForeignKey(BannerPositions, on_delete=models.CASCADE, verbose_name="Banner Position")
    display_order = models.IntegerField(null=True, blank=True)
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=10)
    created_at = models.DateField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name = "Banner"              # singular name in sidebar and forms
        verbose_name_plural = "Banners"

    def __str__(self):
        return self.title
    

