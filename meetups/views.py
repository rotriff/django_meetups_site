from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    meetups =[
        {'title': 'A First Meetup', 
         'location': 'Kyiv', 
         'slug': 'a-first-meetup'},
        {'title': 'A Second Meetup', 
         'location': 'New York',
         'slug': 'a-second-meetup'}
    ]
    return render(request, 'meetups/index.html', {
        'meetups': meetups
    })