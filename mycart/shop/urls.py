from django.urls import path 
from . import views 


urlpatterns = [
    path("",views.index, name='ShopHome'),
    path("about/", views.about, name='ShopAbout'), 
    path("contact/", views.contact, name='ShopContact'),
    path("tracker/", views.tracker, name='ShopTracker'),

    path("search/", views.search, name='ShopSearch'),
    path("products/<int:id>/", views.productView, name='ShopProductView'),
    path("checkout/", views.checkout, name='ShopCheckout'),

] 
