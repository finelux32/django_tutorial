from django import forms
from django.contrib.auth.hashers import check_password

from .models import CommunityUser


class LoginForm(forms.Form):
    user_name = forms.CharField(max_length=20, label="사용자명", error_messages={'required': '아이디를 입력하세요'})
    user_password = forms.CharField(max_length=20, label="비밀번호", widget=forms.PasswordInput,
                                    error_messages={'required': '비밀번호를 입력하세요!!'})

    def clean(self):
        cleaned_data = super().clean()
        print('cleaned_data = ', cleaned_data)
        user_name = cleaned_data.get('user_name')
        user_password = cleaned_data.get('user_password')

        if user_name and user_password:
            user_vo = CommunityUser.objects.get(user_name=user_name)
            if check_password(user_password, user_vo.user_password):
                self.user_id = user_vo.id
            else:
                self.add_error('user_password', '비밀번호가 틀렸습니다!!')
