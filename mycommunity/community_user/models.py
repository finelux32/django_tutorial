from django.db import models


# Create your models here.
class CommunityUser(models.Model):
    user_name = models.CharField(max_length=40, verbose_name="사용자 이름")
    user_password = models.CharField(max_length=40, verbose_name="비밀번호")
    created_datetime = models.DateTimeField(auto_now_add=True, verbose_name="생성시간")

    def __str__(self):
        return self.user_name

    class Meta:
        db_table = 'tb_community_user'
        verbose_name = '커뮤니티 사용자'
        verbose_name_plural = '커뮤니티 사용자'




