from django.shortcuts import render
from store.models import Product
from store.models import ReviewRating

def home(request):
    products= Product.objects.all().filter(is_available=True).order_by('-created_date')
    for single_product in products:
        reviews = ReviewRating.objects.filter(product_id=single_product.id, status=True)
    context={
        'products':products,
        'reviews':reviews,
    }
    return render(request, 'home.html', context)