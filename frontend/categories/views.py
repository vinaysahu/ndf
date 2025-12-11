from django.shortcuts import render, get_object_or_404
from globals.models.Categories import Categories
from globals.models.CategoryMedia import CategoryMedia
from banners.models.Banners import Banners
# from banners.models.BannerPositions import BannerPositions

# Create your views here.
def categories(request):

    banner = Banners.objects.filter(banner_position_id = 1, status=Banners.STATUS_CHOICES_ID['active']).first()
    
    categories = Categories.objects.filter(parent_id_id=None, status=Categories.STATUS_CHOICES_ID['active'])
    
    final_categories = []

    for category in categories:
        subCategories = Categories.objects.filter(parent_id_id=category.id, status=Categories.STATUS_CHOICES_ID['active'])
        hasSubCategory = False
        if subCategories:
            hasSubCategory = True
        final_categories.append({
        "id": category.id,
        "has_sub_category":hasSubCategory,
        "name": category.name,
        "icon": category.icon.url,
        "active":False,
        "sub_categories": list(subCategories)
    })
        
    return render(request, 'frontend/categories/categories.html', {"categories": final_categories,"banner":banner})

def categoryDetail(request, slug):
    banner = Banners.objects.filter(banner_position_id = 1, status=Banners.STATUS_CHOICES_ID['active']).first()
    
    category = get_object_or_404(Categories, slug=slug, status=Categories.STATUS_CHOICES_ID['active'])
    
    final_sub_categories = []

    categoryProducts = CategoryMedia.objects.filter(category_id=category.id)

    subCategories = Categories.objects.filter(parent_id_id=category.id, status=Categories.STATUS_CHOICES_ID['active'])
    hasSubCategory = False

    if subCategories:
        hasSubCategory = True
        for subCategory in subCategories:
            final_sub_categories.append({
                "id": subCategory.id,
                "has_sub_category":False,
                "name": subCategory.name,
                "icon": subCategory.icon.url if subCategory.icon else '',
                "short_description": subCategory.short_description,
                "seo_title": subCategory.seo_title,
                "seo_description": subCategory.seo_description,
                "seo_keywords": subCategory.seo_keywords,
                "active":False,
            })

    final_category = {
        "id": category.id,
        "has_sub_category":hasSubCategory,
        "name": category.name,
        "short_description": category.short_description,
        "description": category.description,
        "seo_title": category.seo_title,
        "seo_description": category.seo_description,
        "seo_keywords": category.seo_keywords,
        "icon": category.icon.url if category.icon else '',
        "image": category.image.url if category.image else '',
        "parent_name": category.parent_id.name if category.parent_id else '',
        "parent_slug": category.parent_id.slug if category.parent_id else '',
        "active":False,
        "sub_categories": final_sub_categories
    }
         
    return render(request, 'frontend/categories/category_details.html', {"category": final_category,"banner":banner,"categoryProducts":categoryProducts})