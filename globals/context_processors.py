from .models.Categories import Categories

def categories_processor(request):
    current_category_slug = request.resolver_match.kwargs.get("slug", None)
    # print("current_category_id",current_category_id)
    categories = Categories.objects.filter(parent_id_id=None, status=Categories.STATUS_CHOICES_ID['active'])
    
    final_categories = [{
        "id": '',
        "has_sub_category":False,
        "name": "Home",
        "link":"/",
        "contact": False,
        "active":False if current_category_slug else True,
        "sub_categories": list()
    }]

    for category in categories:
        subCategories = Categories.objects.filter(parent_id_id=category.id, status=Categories.STATUS_CHOICES_ID['active'])
        hasSubCategory = False

        if subCategories:
            hasSubCategory = True

        final_sub_categories = []
        current_category_id_exit = False

        if current_category_slug == category.slug:
                current_category_id_exit = True

        for subCategory in subCategories:
            if current_category_slug == subCategory.slug:
                current_category_id_exit = True

            final_sub_categories.append({
                "id": subCategory.id,
                "has_sub_category":False,
                "name": subCategory.name,
                "icon": '',
                "contact": False,
                "link":f"/categories/{subCategory.slug}",
                "short_description": '',
                "active":False,
            })

        
        final_categories.append({
            "id": category.id,
            "has_sub_category":hasSubCategory,
            "name": category.name,
            "link":f"/categories/{category.slug}",
            "contact": True,
            "active":current_category_id_exit,
            "sub_categories": final_sub_categories
        })
        # print(final_categories)
    final_categories.append({
            "id": 'contact',
            "has_sub_category":False,
            "name": 'contact',
            "link":f"/contacts",
            "contact": False,
            "active":True if request.path == "/contacts" else False,
            "sub_categories": ''
        })
    return {
        'header_categories': final_categories
    }