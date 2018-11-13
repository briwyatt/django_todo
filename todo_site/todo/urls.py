from django.conf.urls import url
# from django.views.generic import TemplateView, RedirectView

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^visited_list/$', views.visited_list, name='visited_list'),
    url(r'^add/$', views.add_restaurant, name="add"),
    url(r'^delete_restaurant/(?P<restaurant_id>[0-9]+)/$', views.delete_restaurant, name="delete_restaurant"),
    url(r'^check_off_restaurant/(?P<restaurant_id>[0-9]+)/$', views.check_off_restaurant, name='check_off_restaurant')
]

