from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'index.html')

def employee(request):
     return render(request, 'clockIn.html')

def forgotPwd(request):
     return render(request, 'forgotPwd.html')

def adminPage(request):
     return render(request, 'Admin.html')
