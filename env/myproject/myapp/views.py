from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


# Create your views here.

def extract_info(email):
    try:
        validate_email(email)
        username, domain = email.split('@')
        return username, domain
    except ValidationError:
        return None, None

def home(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        username, domain = extract_info(email)
        if username and domain:
            message = f'Hello!!! {username}, you are using email from {domain}.'
        else:
            message = 'Invalid email address. Please try again.'
        return render(request, 'home.html', {'message': message})
    return render(request, 'home.html', {'message':None})