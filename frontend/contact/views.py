from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from globals.models.Feedbacks import Feedbacks
from globals.models.Categories import Categories
import re
from banners.models.Banners import Banners

def is_valid_indian_mobile(number: str) -> bool:
    pattern = r'^(?:\+91[\-\s]?|0)?[6-9]\d{9}$'
    return bool(re.match(pattern, number.strip()))

def contact_submit(request):
    if request.method == 'POST':
        
        name = request.POST.get('name')
        mobile = request.POST.get('phone')
        category_id = request.POST.get('category_id').strip()
        message = request.POST.get('message')

        errorMessages = []

        if not name:
            errorMessages.append("Please enter the name.")

        if mobile:
            if not is_valid_indian_mobile(mobile):
                errorMessages.append("Please enter valid mobile no.")
        else:
            errorMessages.append("Please enter the mobile no.")

        category = None
        if not category_id or not category_id.isdigit():
            errorMessages.append("Please select product.")
        else:
            try:
                category = Categories.objects.get(id=int(category_id))
            except Categories.DoesNotExist:
                errorMessages.append("Please select valid product.")

        if not category:
            errorMessages.append("Please select valid product.")

        if errorMessages:
            for errorMessage in errorMessages:
                messages.warning(request, errorMessage)
            return redirect(request.META.get('HTTP_REFERER', '/')+'#contact')

        try: 
            Feedback = Feedbacks(
                name = name,
                mobile = mobile,
                category_id = category,
                message = message,
            )
            
            Feedback.save()
            messages.success(request, "Your feedback has been submitted successfully.")
        except Exception as e:
            messages.error(request, e)
            messages.error(request, "Something went wrong. Please try again later.")

        return redirect(request.META.get('HTTP_REFERER', '/')+'#contact')
        
    return redirect('/#contact')

def contact(request):

    banner = Banners.objects.filter(banner_position_id = 1, status=Banners.STATUS_CHOICES_ID['active']).first()
        
    return render(request, 'frontend/contact/contact.html', {"banner":banner})
