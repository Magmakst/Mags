from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

def page1(request):
    return render(request, 'main/page1.html')

def page2(request):
    return render(request, 'main/page2.html')

def page3(request):
    return render(request, 'main/page3.html')

def page4(request):
    return render(request, 'main/page4.html')