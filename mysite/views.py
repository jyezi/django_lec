from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import MainContent, Comment
from .forms import CommentForm
from django.core.exceptions import PermissionDenied

# comment update
@login_required(login_url='accounts:login')
def comment_update(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    # raise : 에러를 일으켜 예외 처리
    if request.user != comment.author:
        raise PermissionDenied

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('detail', content_id=comment.content_list.id)

    # 수정 시 최초 작성했던 댓글 화면에 출력
    else:
        form = CommentForm(instance=comment)

    context = {'comment':comment, 'form':form}
    return render(request, 'mysite/comment_form.html', context)

# comment delete
@login_required(login_url='accounts:login')
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.user != comment.author:
        raise PermissionDenied
    else:
        comment.delete()
    return redirect('detail', content_id=comment.content_list.id)

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

# 사용자 댓글
def comment_create(request, content_id):
    content_list = get_object_or_404(MainContent, pk=content_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.content_list = content_list
            comment.author = request.user
            comment.save()
            return redirect('detail', content_id=content_list.id)
    else:
        form = CommentForm()
    context = {'content_list':content_list, 'form':form}
    return render(request, 'mysite/content_detail.html', context)
