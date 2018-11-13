from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import Restaurants
from .forms import TodoForm


def index(request):
    restaurant_list = Restaurants.objects.order_by('id')
    form = TodoForm()
    # context is the things that can be seen on the template
    context = {'restaurant_list': restaurant_list, 'form': form}
    return render(request, 'index.html', context)


def visited_list(request):
    visited_restaurants = Restaurants.objects.filter(visited=True)
    context = {'visited_restaurants': visited_restaurants}
    return render(request, 'visited.html', context)


# this view will only accept POST requests
@require_POST
def add_restaurant(request):
    # text name comes from form field named text
    form = TodoForm(request.POST)
    # take this data and add it to the database
    if form.is_valid():
        new_restaurant = Restaurants(text=request.POST['text'])
        new_restaurant.save()
    return redirect('index')


def delete_restaurant(request, restaurant_id):
    restaurant = Restaurants.objects.get(pk=restaurant_id)
    restaurant.delete()
    return redirect('index')


def check_off_restaurant(request, restaurant_id):
    # get the restaurant by the ID and change its current visit status to visited
    restaurant = Restaurants.objects.get(pk=restaurant_id)
    if not restaurant.visited:
        restaurant.visited = True
    restaurant.save()
    return redirect('index')


