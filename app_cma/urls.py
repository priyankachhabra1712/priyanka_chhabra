from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('contact_add', views.contact_add, name='contact_add'),
    path('show_details/<contact_id>', views.show_details, name='show_details'),
    path('delete_contact/<contact_id>', views.delete_contact, name='delete_contact'),
    path('delete/<contact_id>', views.delete, name='delete'),
    path('update/<contact_id>', views.update, name='update'),
    ]