# Create your views here.
from django.shortcuts import render, redirect
from .models import Contacts
from django.contrib import messages
import datetime
from .form import formCon
def landing_page(request):
    all_contacts = Contacts.objects.all()
    return render(request, 'landing_page.html', {'all_contacts': all_contacts})

def create_time():
    time = datetime.datetime.now().strftime('%b %d, %Y, %H:%M')
    return time


def delete_contact(request, contact_id):
    curr_contact = Contacts.objects.get(pk=contact_id)
    return render(request, 'delete_contact.html', {'curr_contact': curr_contact})

def delete(request, contact_id):
    curr_contact = Contacts.objects.get(pk=contact_id)
    curr_contact.delete()
    return redirect('landing_page')

def contact_add(request):
    if request.method == 'POST':

        form = formCon(request.POST or None)

        if form.is_valid():
            print(form["contact_email"].value())
            if Contacts.objects.filter(contact_email=form['contact_email'].value()):
                messages.success(request, ('Contact with this E-mail id already exists! Please try again.'))
                return redirect('contact_add')
            elif Contacts.objects.filter(contact_name=form['contact_name'].value()):
                messages.success(request, ('Contact with this name already exists! Please try again.'))
                return redirect('contact_add')
            else:
                form.save()
                messages.success(request, ('Contact created successfully.'))
                return redirect('landing_page')
        else:
            # prints error for debugging
            print(form.errors)
    else:
        form = formCon()

    return render(request, 'contact_add.html', {'form': form,'created_time': create_time()})

def show_details(request, contact_id):
    curr_contact = Contacts.objects.get(pk=contact_id)
    print(curr_contact)
    return render(request, 'show_details.html', {'curr_contact': curr_contact})