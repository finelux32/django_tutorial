from django.db import models

# Create your models here.
from django.db.models import CharField, TextField, DateTimeField


class Board(models.Model):
    subject = CharField(max_length=40, verbose_name="제목")
    author = CharField(max_length=40, verbose_name="작성자")
    contents = TextField(verbose_name="내용")
    created_time = DateTimeField(auto_now_add=True, verbose_name="등록시간")
    
    def __str__(self):
        return self.subject

    class Meta:
        db_table = 'tb_board'
        verbose_name = '게시물'
        verbose_name_plural = '게시물'

