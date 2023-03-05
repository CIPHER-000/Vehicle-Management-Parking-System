from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect

def index(request):
    return render(request, 'adminPage.html')

@csrf_protect
def login(request):
    return render(request, 'admin_login.html')
