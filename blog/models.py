from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = "blog/", blank=True, null=True)

    #객체가 호명될때 어떠한 이름으로 호명이 될지 정해줌 / 아래는 각각의 객체의 title값으로 호명이 되게 해둠
    def __str__(self):
        return self.title
    #body값의 내용이 너무 길면 보기가 안좋아서 클래스 안에 summary라는 새로운 함수를 만들어서 사용함
    def summary(self):
        return self.body[:100]