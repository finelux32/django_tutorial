import json

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import CommunityUser


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
        user_name = request.POST['userName']
        user_password = request.POST['password']
        community_user = CommunityUser(user_name=user_name, user_password=user_password)
        community_user.save()

        response_obj = {'resp_msg': '회원가입, 성공적', 'resp_code': 0}

        return render(request, 'signup.html', response_obj)


def restapi_test(request):
    if request.method == 'GET':
        sample_json_dict = {'hello': "world", 'ga': 'zua!!'}
        sample_json = json.dumps(sample_json_dict)
        return HttpResponse(sample_json, content_type="application/json")



