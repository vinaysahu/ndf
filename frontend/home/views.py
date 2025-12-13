from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from globals.models.Categories import Categories
from banners.models.Banners import Banners
from common.googleReview.reviews import GetReviews
# from banners.models.BannerPositions import BannerPositions

# Create your views here.
def home(request):
    # ... 8510033759
    reviews = GetReviews(10)
    
    banner = Banners.objects.filter(banner_position_id = 1, status=Banners.STATUS_CHOICES_ID['active']).first()
    
    categories = Categories.objects.filter(parent_id_id=None, status=Categories.STATUS_CHOICES_ID['active'])
    return render(request, 'frontend/home/home.html', {"categories": categories,"banner":banner,"reviews":reviews})

