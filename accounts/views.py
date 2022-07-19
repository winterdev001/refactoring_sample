from django.shortcuts import render
from django.contrib.auth.models import User

def index(request):
    users = User.objects.all()
    params = {'users':users}
    return render(request,'accounts/index.html', params)

