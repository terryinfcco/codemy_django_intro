from django.shortcuts import render

# Create your views here.

def home(request):
    company_name = 'TedCo'
    return render(request, "home.html", {"company_name": company_name})

def about(request):
    company_name = 'TedCo'
    return render(request, "about.html", {"company_name": company_name})
