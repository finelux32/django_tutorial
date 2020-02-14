# Create your views here.
from django.shortcuts import render, redirect


def home(request):
    if 'user_id' in request.session:
        print(request.session)
        logged_in_user_name = request.session['user_id']
        return render(request, 'home.html', {'user_id': logged_in_user_name})
    return render(request, 'home.html')
