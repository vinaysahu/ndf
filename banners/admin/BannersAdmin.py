from django.contrib import admin
from ..models.Banners import Banners
from django.utils.html import format_html
from common.filters.adminModelFilter import SameTableParentFilter
        
class BannersAdmin(admin.ModelAdmin):

    list_display = ["title", "show_image", "created_at", "updated_at" ] # grid mae kaisa view
    exclude = ('created_at', 'updated_at')       # Remove from FORM

    def show_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return "—"

    show_image.short_description = "Image"

    
    

admin.site.register(Banners,BannersAdmin)
