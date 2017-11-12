# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class Data:
    def generate(count):
        data = []
        for i in range(1, count):
            data.append(
                {
                    'nickname': 'name' + str(i),
                    'qheader': 'Head' + str(i),
                    'qtext': 'Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut                      fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed odio dui.',
                    'likes': i,
            }
        )
        return data

class PaginatorClass():
    @staticmethod
    def paginate(data, page):
        paginator = Paginator(data, 10)
        try:
            return paginator.page(page)
        except PageNotAnInteger:
            return paginator.page(1)
        except EmptyPage:
            return paginator.page(paginator.num_pages)

# Create your views here.
def Auth(request):
    return render(request, 'Auth.html', {})

def MainPage(request):
    page = request.GET.get('page')
    data = Data.generate(500)
    dat = PaginatorClass.paginate(data, page)
    # on_page=pages.page(pagenum).object_list
    return render(request, 'MainPage.html', {'data': dat,})


def Tagged(request):
    return render(request,'tagged.html',  {})
def auth(request):
    return render(request,'auth.html', locals())
def Debate(request):
    return render(request,'Debate.html', locals())
def Discussion(request):
    return render(request,'Discussion.html', locals())
def Registration(request):
    return render(request,'registration.html', locals())
def Settings(request):
    return render(request, 'Settings.html', locals())
def Hot(request):
    return render(request, 'hot.html', {'data' : Data.generate(50)})

