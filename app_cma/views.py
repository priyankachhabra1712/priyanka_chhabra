# Create your views here.
from django.shortcuts import render, redirect
from .models import Contacts
from django.contrib import messages
import datetime

def landing_page(request):
    all_contacts = Contacts.objects.all()
    return render(request, 'landing_page.html', {'all_contacts': all_contacts})

def create_time():
    time = datetime.datetime.now().strftime('%b %d, %Y, %H:%M')
    return time

def landing_page(request):
    all_contacts = Contacts.objects.all()
    return render(request, 'landing_page.html', {'all_contacts': all_contacts})

def contact_add(request):
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            print(form["contact_email"].value())
            if Contacts.objects.filter(contact_email=form['contact_email'].value()):
                messages.success(request, ('Contact with this E-mail id already exists! Please try again.'))
                return redirect('contact_add')
            else:
                form.save()
                messages.success(request, ('Contact created successfully.'))
                return redirect('landing_page')
    else:
        return render(request, 'contact_add.html', {'created_time': create_time()})