import os
import django
import random
from .models import *

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ask_kbritikov.settings")
nicks=["Maginot","Churchill","Hitler","Josef","Roosevelt","Hirohito","Mussolini","Mao","Tito","Golle","Mannergeim","Franko","Ataturk"]
arts=["Super","Mega","Perfect","Soviet","Nazi","Free","Elite","New"]
class Filler:
    def cAuthor(self):
        n=random.choice(arts)+" "+random.choice(nicks)
        obj = User(email=n+"@email.net",username=n)
        obj.save()
        aobj=Author(user=obj,nickname=n,img='images.duckduckgo.com.png')
        aobj.save()

    def cQuestion(self):
        obj=Question(id(Question),head='Reich will rise!!!',user=random.choice(Author.objects.all()),text="Mein Kampf!!! Das Reich!! Deuchland Uber alles!!",pub_date=datetime.datetime.today())
        obj.save()
        obj.tags.add(random.choice(Tag.objects.all()))
        obj.tags.add(random.choice(Tag.objects.all()))
        obj.save()


    def cAnswer(self):
        obj=Answer(user=random.choice(Author.objects.all()), post=random.choice(Question.objects.all()),text="Mein Kampf!!! Das Reich!! Deuchland Uber alles!!",pub_date=datetime.datetime.today())
        obj.save()


    def cTag(self):
        obj=Tag(tagtext=random.choice(nicks))
        obj.save()

    def cLike(self):
        obj=Like(user=random.choice(Author.objects.all()),post=random.choice(Question.objects.all()),rate=random.randint(0,1))
        obj.save()
	# for i in range(10):
	# 	obj = Author();
	# 	obj.nickname='Nick_'+str(i)
	# 	obj.email='Nick_'+str(i)+'@email.net'
	# 	obj.image='picture'
	# 	obj.save()
