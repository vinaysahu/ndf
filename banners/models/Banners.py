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
    
    INITIAL_DATA=[
  {
    "id": 1,
    "title": "Beautiful Spaces Begin With Us",
    "image": "images/banners/banner-bg.jpg",
    "link_url": "ddasd",
    "btn_title": "Learn More",
    "description": "Looking for curtains, blinds, wallpapers, fabrics, or upholstery?\r\nStart by browsing our categories and discover the best options for your home.",
    "display_order": 1,
    "status": 10,
    "banner_position_id_id": 1
  },
  {
    "id": 2,
    "title": "Second Slide Title",
    "image": "images/banners/banner-bg_yH6uvTe.jpg",
    "link_url": "dsfdf",
    "btn_title": "Learn More",
    "description": "Explore thoughtfully curated decor essentials that elevate every room. From fabrics to flooring, experience style, comfort & luxury in one place.",
    "status": 10,
    "banner_position_id_id": 1
  },
  {
    "id": 3,
    "title": "Third Slide Title",
    "image": "images/banners/banner-bg_AkimyA8.jpg",
    "description": "Explore thoughtfully curated decor essentials that elevate every room. From fabrics to flooring, experience style, comfort & luxury in one place.",
    "status": 10,
    "banner_position_id_id": 1
  }
]
    

