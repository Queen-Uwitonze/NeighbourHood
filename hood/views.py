from django.shortcuts import render

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
   

    message = "welcome"
    return render(request, 'home.html',{"message":message})
