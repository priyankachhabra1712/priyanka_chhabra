from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('contact_add', views.contact_add, name='contact_add'),
    ]