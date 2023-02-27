from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect

from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request,'base.html')

@csrf_protect
def login(request):
    return render(request, 'admin_login.html')
