
from django.shortcuts import render, get_object_or_404, redirect
from django import forms
from contact.forms import ContactForm 
from contact.models import Contact


def create(request):
    if request.method == 'POST':
        context = {
            'form': ContactForm(request.POST)

        }
        return render(
            request,
        'contact/create.html',
        context
        )
     
    context = {
    'form': ContactForm()

    }
    return render(
        request,
        'contact/create.html',
        context
        )   
       