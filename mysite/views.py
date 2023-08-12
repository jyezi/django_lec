from django.shortcuts import render
from .models import MainContent

def index(request):
    # return HttpResponse("Hello World!");
    content_list = MainContent.objects.order_by('-pub_date');
    context = {'content_list':content_list}

    # render : context_list를 mysite/content_list.html 파일에 적용 후 HTML을 리턴
    return render(request, 'mysite/content_list.html', context)