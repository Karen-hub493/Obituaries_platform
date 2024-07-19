# obituaries/views.py
from django.shortcuts import render, redirect
from .models import Obituary
from django.utils.text import slugify
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.utils import timezone
from django import forms
import logging

logger = logging.getLogger(__name__)

class ObituaryForm(forms.ModelForm):
    class Meta:
        model = Obituary
        fields = ['name', 'date_of_birth', 'date_of_death', 'content', 'author']

def generate_unique_slug(name, date_of_death):
    base_slug = slugify(f"{name}-{date_of_death}")
    slug = base_slug
    counter = 1
    
    while Obituary.objects.filter(slug=slug).exists():
        slug = f"{base_slug}-{counter}"
        counter += 1
    
    return slug

def submit_obituary(request):
    if request.method == 'POST':
        form = ObituaryForm(request.POST)
        
        if form.is_valid():
            name = form.cleaned_data['name']
            date_of_death = form.cleaned_data['date_of_death']
            
            slug = generate_unique_slug(name, date_of_death)
            
            try:
                obituary = form.save(commit=False)
                obituary.slug = slug
                obituary.full_clean()  # Validate the model instance
                obituary.save()
                return HttpResponse('Obituary submitted successfully')
            except ValidationError as e:
                logger.error(f"Validation error: {e.messages}")
                return HttpResponse(f"Validation error: {e.messages}", status=400)
            except IntegrityError as e:
                logger.error(f"Integrity error: {e}")
                return HttpResponse("Error saving the obituary. Please try again.", status=500)
        else:
            return render(request, 'obituary_form.html', {'form': form})
    
    form = ObituaryForm()
    return render(request, 'obituary_form.html', {'form': form})

def view_obituaries(request):
    obituaries = Obituary.objects.all()
    return render(request, 'view_obituaries.html', {'obituaries': obituaries})
