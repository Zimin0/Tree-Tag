from django.shortcuts import render

""" Страницы для первого меню """
def page0(request):
    return render(request, "test_pages_app/test.html")

def page1(request):
    return render(request, "test_pages_app/test.html")

def page2_1(request):
    return render(request, "test_pages_app/test.html")

def page2_1_1(request):
    return render(request, "test_pages_app/test.html")

def page2(request):
    return render(request, "test_pages_app/test.html")

def page3(request):
    return render(request, "test_pages_app/test.html")

def page4(request):
    return render(request, "test_pages_app/test.html")
"""---------------------------"""

""" Страницы для второго меню """
def info0(request):
    return render(request, "test_pages_app/test.html")

def info1(request):
    return render(request, "test_pages_app/test.html")
"""---------------------------"""