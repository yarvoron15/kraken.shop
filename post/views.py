from django.shortcuts import render, HttpResponse
import random
from datetime import datetime

# Create your views here.


jokes = ["Не спрашивай у мужчины про его доходы, у женщины про возраст, у патриота, откуда у него американский паспорт.",
         'Мужик долго выбирает шляпу в магазине, на прилавке одни "котелки" типа чаплинского. Мужик продавщице: - Че у вас все шляпы такие хуевые?! Продавщица, ударяя ребром ладони по "котелку": - Не нравятся хуевые - возьмите пиздатую',
         'колобок повесился']
random_joke = random.choice(jokes)
def hello_view(request):
    if request.method == 'GET':
        return HttpResponse('Hello, World!')

def home_view(request):
    if request.method == 'GET':
        current_date = datetime.now().date()
        current_time = datetime.now().time()

        context = {
            'current_date': current_date,
            'current_time': current_time,
        }
        return render(request, 'home.html', context)


def fun_view(request):
    if request.method == 'GET':
        return HttpResponse( random_joke)