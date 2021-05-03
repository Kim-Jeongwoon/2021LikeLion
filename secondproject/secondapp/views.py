from django.shortcuts import render

# Create your views here.

def introduce(request):
    return render(request, '자기소개index.html')

def introduce1(request):
    return render(request, '자기소개index.html')

def history(request):
    return render(request, '연혁.html')

def tmi(request):
    return render(request, 'tmi.html')

def contact(request):
    return render(request, '연락처.html')