from django.shortcuts import render, get_object_or_404
from .models import MainContent

def index(request):
    # return HttpResponse("Hello World!");
    content_list = MainContent.objects.order_by('-pub_date');
    context = {'content_list':content_list}

    # render : context_list를 mysite/content_list.html 파일에 적용 후 HTML을 리턴
    return render(request, 'mysite/content_list.html', context)

# 상세화면을 위한 추가 코드 (상세보기)
def detail(request, content_id):
    content_list = get_object_or_404(MainContent, pk=content_id) # content_list가 없으면 404오류 안내
    #content_list = MainContent.objects.get(id=content_id)
    context = {'content_list':content_list}
    return render(request, 'mysite/content_detail.html', context)