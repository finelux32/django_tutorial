from django.shortcuts import render
from .forms import BoardWriteForm
from .models import Board
from community_user.models import CommunityUser


def readBoard(request, pk):
    board_data = Board.objects.get(pk=pk)
    return render(request, "board_detail.html", {'board_data':board_data})


def writeBoard(request):
    if request.method == 'GET':
        form = BoardWriteForm()
        return render(request, 'board_write.html', {'board_write_form': form})
    elif request.method == 'POST':
        board_write_form = BoardWriteForm(request.POST)
        if board_write_form.is_valid():
            subject = board_write_form.subject
            contents = board_write_form.contents

            user_id = request.session.get('user_id')
            community_user = CommunityUser.objects.get(id=user_id)
            author = community_user.user_name

            board_item = Board(subject=subject, contents=contents, author=author)
            board_item.save()
        board_data_list = Board.objects.all().order_by('-id')
        return render(request, 'board.html', {'board_data_list': board_data_list})


def articles(request):
    board_data_list = Board.objects.all().order_by('-id')
    print(board_data_list)
    return render(request, 'board.html', {'board_data_list': board_data_list})
