from django.shortcuts import redirect


def login_check(function):
    def wrapper(request, *args, **kwargs):
        user = request.session.get('user_id')
        if user is None or not user:
            return redirect('/community_user/login')
        return function(request, *args, **kwargs)
    return wrapper

