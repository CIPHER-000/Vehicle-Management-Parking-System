from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect

def index(request):
    return render(request, 'adminPage.html')

@csrf_protect
def login(request):
    return render(request, 'admin_login.html')
def dash(request):
    return render(request,'dash.html')
def userLogin(request):
    return render(request,'userLogin.html')
def userLoginPage(request):
    return  render(request,'user_login_page.html')

def userPage(request):
    return render(request,'user_page_view.html')

def userSignup(request):
    return render(request,'userSignup.html')
