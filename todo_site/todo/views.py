from django.shortcuts import render
from .models import Restaurants

def index(request):
    restaurant_list = Restaurants.objects.order_by('id')

    context = {'restaurant_list': restaurant_list}

    return render(request, 'index.html', context)
