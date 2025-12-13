import requests
from django.http import JsonResponse

# Create your views here.
def GetReviews(page_length=10):
    
    url = f"https://service-reviews-ultimate.elfsight.com/data/reviews?uris%5B%5D=ChIJ9dB_hFEXDTkRiKTwFJwIPcM&filter_content=text_required&min_rating=4&page_length={page_length}&order=date"
    response = requests.get(url)
    data = []
    if response.status_code == 200:
        res = response.json()   # JSON ko Python dict/list me convert
        if "result" in res:
            if "data" in res['result']:
                data = res['result']['data']
    
    return data
    

