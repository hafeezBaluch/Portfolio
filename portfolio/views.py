from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def about_me(request):
    return render(request,'about_me.html')
