# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random
import string
import datetime
from django.core import serializers
from django.http import *
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
from .fMods import *
from .forms import *
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.views.generic import *
from django.shortcuts import render_to_response

# def login_required(function_to_decorate):
#     # Внутри себя декоратор определяет функцию-"обёртку". Она будет обёрнута вокруг декорируемой,
#      # получая возможность исполнять произвольный код до и после неё.
#     def the_wrapper_around_the_original_function():
#         if
#         function_to_decorate() # Сама функция
#         print("А я - код, срабатывающий после")
#      return the_wrapper_around_the_original_function

def generate(count):
        data = []
        for i in range(1, count):
            data.append(
                {
                    'nickname': 'name' + str(i),
                    'qheader': 'Head' + str(i),
                    'qtext': 'Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut                      fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed odio dui.',
                    'likes': i,
                    'tags':'Tag'+ str(i)
            }
        )
        return data

def exit(request):
    logout(request)
    return  HttpResponseRedirect("/")

def paginate(data, request):
   page=request.GET.get('page',1)
   paginator = Paginator(data, 10)
   try:
        return paginator.page(page)
   except PageNotAnInteger:
        return paginator.page(1)
   except EmptyPage:
        return paginator.page(paginator.num_pages)

   # Create your views here.
def mod_log(request):
     form = LogF()
     templ_n = "modal.html"
     success_url = "/"
     error = 0
     items = dict(not_exist=True)
     return render(request, 'modal.html', locals())

#def modal(request):

# Create your views here.
# def log(request):
#     form=LogF()
#     templ_n = "auth.html"
#     success_url = "/"
#     error = 0
#     if request.method =='POST':
#         log=request.POST.get('nickname')
#         if not (User.objects.filter(author__nickname=log).exists()) :
#             error=1
#             return render(request, 'auth.html', locals())
#         password=request.POST.get('password')
#         user=authenticate(username=log, password=password)
#         if user is not None:
#             print("NOT NONE")
#             if user.is_active:
#                 login(request,user)
#                 response = HttpResponseRedirect(success_url)direct_to_template(request, template, context, 'text/javascript')

#                 return response
#             else:
#                 print("NOT ACTIVE")
#                 tems = dict(not_active=True)
#                 return render(request, 'auth.html', locals())
#         else:
#             print("IS NONE")
#             items = dict(not_exist=True)
#             return render(request, 'auth.html', locals())
#     else:
#         print("NO DATA")
#         return render(request,'auth.html',locals())

def log(request):
    form=LogF()
    templ_n = "auth.html"
    success_url = ""
    error = 0
    if request.method =='POST':
        log=request.POST.get('nickname')
        if not (User.objects.filter(author__nickname=log).exists()) :
            error=1
            return render(request, 'auth.html', locals())
        password=request.POST.get('password')
        user=authenticate(username=log, password=password)
        if user is not None:
            print("NOT NONE")
            if user.is_active:
                login(request,user)
                response = HttpResponseRedirect('/')
                return response
            else:
                print("NOT ACTIVE")
                tems = dict(not_active=True)
                return render(request, 'auth.html', locals())
        else:
            print("IS NONE")
            items = dict(not_exist=True)
            return render(request, 'auth.html', locals())
    else:
        print("NO DATA")
        return render(request,'auth.html',locals())


def generate_long_random_key():
    letters = string.printable
    return ''.join(random.choice(letters) for i in range(20))


def like(request):
    if not request.user.is_authenticated:
        response = HttpResponseRedirect('/')
        return response
    if request.method == 'POST':
        user = User.objects.get(username=request.POST.get('user'))
        quest = Question.objects.get(id=int(request.POST.get('question')))
        print(request.POST.get('positive'))
        if request.POST.get('positive') == 'true':
            print('positive')
            try:
                lk = Like(post=quest, user=user.author, rate=True)
                lk.save()

                return JsonResponse({'total_likes': quest.total_likes()}, status=200)
            except:
                return JsonResponse({'ErrorMSG': "Alredy liked"}, status=403)

        else:
            try:
                print('negative')
                lk = Like(post=quest, user=user.author, rate=False)
                lk.save()
                return JsonResponse({'total_likes': quest.total_likes()}, status=200)
            except:
                return JsonResponse({'ErrorMSG': "Already disliked"}, status=403)
    return HttpResponse()


def scroll(request):
    print('inscroll')
    data = Question.objects.all()
    page = paginate(data, request)

    data=HttpResponse('lst.html',{'data':page}).serialize()
    # data='lst.html'
    # data=data%page
    # try:
    print('pagination done')
    return render(request,'lst.html',{'data':page})
    # except:
    #     print('err')
    #     return JsonResponse({'ErrorMSG':"Some shit happened"},status=400)

def main_new(request):
    data = Question.objects.all()
    page = paginate(data, request)
    return render(request, 'main.html', {'data': page})
    # numbers_list = Question.objects.all()
    # page = request.GET.get('page', 1)
    # paginator = Paginator(numbers_list, 5)
    # try:
    #     numbers = paginator.page(page)
    # except PageNotAnInteger:
    #     numbers = paginator.page(1)
    # except EmptyPage:
    #     numbers = paginator.page(paginator.num_pages)
    # return render(request, 'main.html', {'data': numbers})
    # # data=Question.objects.all()
    # # if(request.method=='POST'):
    # #     print('ispost')
    # #     page = paginate(data,request)
    # #     return JsonResponse({'pag':list(page.object_list)},safe=False,status=200)
    # # else:
    #     page = paginate(data, request)
    #     return render(request, 'main.html', {'data': page})


#@require_POST
#@login_required
def vote(request):
   try:
    qid=int(request.POST.get('qid'))
   except:
       return JsonResponse(dict(error="er"))
   vote=request.POST.get('vote')
   question=Question.objects.get(qid)
   if vote=='inc':
       question.rating+=1;
       question.save()
   if vote=='dec':
       question.rating-=1
       question.save()
   return JsonResponse(dict(ok=1))

#@login_required
def profile(request):
    profile=request.user.author
    print(profile.user.username)
    if request.POST:
        form=AuthF(request.POST,request.FILES)
        if form.is_valid():
            print("All right!")
            profile.img=form.cleaned_data['img']
            profile.save()
    return render(request,'profile.html',{})



class Tagged(TemplateView):
    template_name = 'tagged.html'
    model=Question
    def get(self,request):
        obj=Filler()
    # obj.cAuthor()
    # obj.cTag()
    # obj.cQuestion()
    # obj.cAnswer()
    # obj.cLike()
        tag =Tag.objects.get(tagtext= request.GET.get('tag'))
        data = Question.objects.filter(tags=tag)
        tagged=None
        data = paginate(data,request)
        return render(request,'tagged.html',locals())

def Debate(request):
    if not request.user.is_authenticated:
        response = HttpResponseRedirect('/')
        return response
    form = DebF()
    us=request.user
    if request.method=="POST":
        hd = request.POST.get('head')
        if hd is None:
            return render(request, 'debate.html', locals())
        text=request.POST.get('text')
        img=request.FILES.get('image')
        if text is None:
            return render(request, 'debate.html', locals())
        quest = Question(head=hd, text=text, user=us.author,image=img)
        quest.save()
        tags=request.POST.get('tags').split(",")
        tag=0
        taged=[]
        for i in tags:
            tag=Tag.objects.filter(tagtext=i)
            if not tag.exists():
                tag=Tag(tagtext=i)
                tag.save()
                quest.tags.add(tag)
                break
            for j in tag:
                quest.tags.add(j)
        quest.save()
        response = HttpResponseRedirect('/question?question='+str(quest.id))
        return response

    return render(request,'debate.html', locals())

def Discussion(request):
    form=AnsF()
    question = Question.objects.get(id=request.GET.get('question'))

    data = Answer.objects.filter(post_id=question.id)
    data=paginate(data,request)
    if request.method == 'POST':
        text=request.POST.get('text')
        if text is None:
            return render(request, 'registration.html', locals())
        ans=Answer(text=text,user=request.user.author,post=question)
        ans.save()
        return render(request, 'discussion.html', locals())
    return render(request,'discussion.html', locals())


# class New(View, JsonResponseMixin, TemplateResponseMixin):
#     def get_context(self, request):
#         pass
#
#     def get(self, request, *args, **kwargs):
#         context = self.get_context(request)
#         if request.GET.get('format', 'html') == 'json' or self.template_name is None:
#             return JsonResponseMixin.render_to_reponse(self, context)
#         else:
#             return TemplateResponseMixin.render_to_response(self, context)


def Registration(request):
    if request.user.is_authenticated:
        response = HttpResponseRedirect('/')
        return response
    form = RegF()
    templ_n = "registration.html"
    success_url = "/"
    error=0
    if request.method == 'POST':
        nickname=request.POST.get('nickname')
        if nickname is None:
           error=1
           return render(request, 'registration.html', locals())
        password=request.POST.get('password')
        if password is None:
           error=2
           return render(request, 'registration.html', locals())
        cpassword = request.POST.get('chPassword')
        if password != cpassword:
            error = 3
            return render(request, 'registration.html', locals())
        email = request.POST.get('email')
        if email is None:
           error=4
           return render(request, 'registration.html', locals())
        image =request.FILES.get('image')
        user=User(email=email,username=nickname)
        user.set_password(password)
        if((User.objects.filter(email=email).exists()) or (User.objects.filter(username=nickname).exists())):
            error=5
            return render(request, 'registration.html', locals())
        else:
            user.save()
        author=Author(nickname=nickname,img=image, user=user)
        author.save()
        response = HttpResponseRedirect('/')
        return response


    else:
        print("NO DATA")
        return render(request, 'registration.html', locals())


def Settings(request):
    if not request.user.is_authenticated:
        response = HttpResponseRedirect('/')
        return response

    form=SetF()
    us=request.user
    if request.method == 'POST':
        nickname = request.POST.get('nickname')
        if nickname is not '':
            us.author.nickname = nickname
        log = request.POST.get('login')
        if log is not '':
            us.username = log
        email = request.POST.get('email')
        if email is not '':
            us.email = email
        image = request.FILES.get('image')
        if image is not None:
            us.author.img = image
        us.save()
        us.author.save()
    return render(request, 'settings.html', locals())


def Hot(request):
    data=Question.objects.all()
    return render(request, 'hot.html', {'data' : data})

