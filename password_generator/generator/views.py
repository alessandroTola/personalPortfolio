from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request, 'generator/home.html', {'password':'sdfdfdfdf'})

def password(request):
    #thepassword = request.GET['password']
    #characters = list(request.GET['uppercase'], request.GET['numbers'], request.GET['spacial'])
    characters = list('abcdefghijklmnopqrstuvwxyz')
    password = ''
    
    if(request.GET.get('uppercase')):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    if(request.GET.get('special')):
        characters.extend(list('!#@%&$?()^'))
        
    if(request.GET.get('numbers')):
        characters.extend(list('1234567890'))    
    
    length = int(request.GET.get('length'))
    for x in range(0, length):
        password += random.choice(characters)
        
    return render(request, 'generator/password.html', {'password':password})