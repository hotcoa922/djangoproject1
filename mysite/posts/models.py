from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    writer = models.CharField(max_length=50)
    content = models.TextField()    #내용을 저장하는 필드, 글자수 제한 없음

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):  #admin들어갔을때 쉽게 구분위해 사용
        return self.title


        