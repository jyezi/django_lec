from django.shortcuts import render

def mainpage(request):
    return render(request, 'pages/mainpage.html')
def company(request):
    return render(request, 'pages/company_info.html')
def service(request):
    return render(request, 'pages/service.html')
def product(request):
    return render(request, 'pages/product.html')
def card(request):
    return render(request, 'mysite/content_list.html')
def cs(request):
    return render(request, 'pages/cs.html')
def greeting(request):
    return render(request, 'pages/company_greeting.html')
def history(request):
    return render(request, 'pages/company_history.html')