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

def meetup_details(request, meetup_slug):
    selected_meetup = {
        'title': 'A Meetup', 
        'description': 'This is a meetup!'
        }
    return render(request, 'meetups/meetup-detail.html', {
        'meetup_title': selected_meetup['title'],
        'meetup_description': selected_meetup['description']
    })