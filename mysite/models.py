from django.db import models
from django.contrib.auth.models import User

class MainContent(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')
    
    # title을 object 형태(Main Conent Object)가 아닌 문자열(실제 제목)로 반환
    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content_list = models.ForeignKey(MainContent, on_delete=models.CASCADE) # 메인컨텐츠 삭제 시, comment도 삭제
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
