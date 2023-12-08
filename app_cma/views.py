# Create your views here.
from django.shortcuts import render, redirect
from .models import Contacts
from django.contrib import messages
from datetime import datetime

def landing_page(request):
    all_contacts = Contacts.objects.all()
    return render(request, 'landing_page.html', {'all_contacts': all_contacts})

