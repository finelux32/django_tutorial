from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect

# Create your views here.
from .forms import LoginForm
from .models import CommunityUser


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
        user_name = request.POST['userName']
        user_password = request.POST['userPassword']
        user_password_check = request.POST['passwordCheck']
        user_email = request.POST['userEmail']

        # Validation
        response_data = {}
        if not (user_name and user_password and user_password_check and user_email):
            response_data['error_message'] = '모든 정보를 입력하세요.'
        if user_password != user_password_check:
            response_data['error_message'] = '비밀번호가 일치하지 않습니다.'
        else:
            # encryption
            encrypted_password = make_password(user_password)
            community_user = CommunityUser(user_name=user_name, user_password=encrypted_password, user_email=user_email)
            community_user.save()
            response_data['register_success_message'] = '회원가입이 완료되었습니다.'
        return render(request, 'signup.html', response_data)


def login(request):
    login_form = None
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_id = login_form.user_id
            request.session['user_id'] = user_id
            return redirect('/')
    else:
        login_form = LoginForm()
    return render(request, 'login.html', {'login_form': login_form})


def logout(request):
    if request.session.get('user_id'):
        del (request.session['user_id'])  # remove Key & Value in dict
    return redirect('/')


def home(request):
    if 'user_id' in request.session:  # request.session dictionary > Key Check
        user_id = request.session['user_id']
        user_vo = CommunityUser.objects.get(pk=user_id)
        return render(request, 'board.html', {'user_name': user_vo.user_name})
    else:
        return render(request, 'board.html')
