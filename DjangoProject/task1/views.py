from django.shortcuts import render
from .models import *

# Create your views here.


def home_page(request):
    return render(request, 'home_page.html')


def catalog(request):
    title = 'Игры'
    games = Game.objects.all()
    context = {'title': title,
               'games': games}
    return render(request, 'catalog.html', context)


def my_games(request):
    return render(request, 'my_games.html')


def sign_up_by_html(request):
    users = Buyer.objects.all()
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        balance = request.POST.get('balance')
        try:
            age = int(request.POST.get('age'))
            if age < 1:
                info['error'] = 'Такого возраста не бывает'
            elif username in username_list(users):
                info['error'] = 'Пользователь уже существует'
            else:
                info['message'] = f'Приветствуем, {username}!'
                Buyer.objects.create(name=username,
                                     balance=balance,
                                     age=age)
        except TypeError:
            info['error'] = 'Возраст должен быть натуральным числом'
    else:
        info['error'] = 'Данные некорректны'
    return render(request, 'registration_page.html', info)


def username_list(users: list[Buyer]):
    result_list = []
    for user in users:
        result_list.append(str(user.name))
    return result_list
