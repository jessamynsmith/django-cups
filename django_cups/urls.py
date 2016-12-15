from django.conf.urls import url

from django_cups import views


urlpatterns = [
    url(r'^displayPrintForm/$', views.displayPrintForm, name='displayPrintForm'),
    url(r'^getPrinterslist/$', views.getPrinterslist, name='getPrinterslist'),
    url(r'^refreshPrinterslist/$', views.refreshPrinterslist, name='refreshPrinterslist'),
    url(r'^favourites/getlist/$', views.getFavouriteslist, name='getFavouriteslist'),
    url(r'^favourites/add/(?P<printer_id>\d+)$', views.addFavourite, name='addFavourite'),
    url(r'^favourites/del/(?P<printer_id>\d+)$', views.delFavourite, name='delFavourite'),
]
