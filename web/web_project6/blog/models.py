from django.db import models

# Create your models here.

class Post(models.Model):
    id = models.BigAutoField("id", primary_key=True)
    title = models.CharField("제목", max_length = 30)
    content = models.TextField("내용")
    created_at = models.DateTimeField("작성일", auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return f"[{self.id}]{self.title}"