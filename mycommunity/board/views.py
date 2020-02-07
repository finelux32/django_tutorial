from django.shortcuts import render


# Create your views here.
from .models import Board


def articles(request):
    board_data_list = Board.objects.all().order_by('-id')
    print(board_data_list)
    return render(request, 'board.html', {'board_data_list': board_data_list})

