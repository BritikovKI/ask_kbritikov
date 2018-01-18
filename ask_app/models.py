from __future__ import unicode_literals
import datetime
from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    nickname = models.CharField(max_length=10)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    img=models.ImageField(blank=True,verbose_name='Avatar',upload_to="uploads/" )
    def __str__(self):
        return 'Author: {}'.format(self.nickname)


class Tag(models.Model):
     tagtext=models.CharField(max_length=10,unique=True)

     def __str__(self):
         return 'Tag: {}'.format(self.tagtext)




class Question(models.Model):
    user=models.ForeignKey(Author)
    text=models.TextField()
    head=models.CharField(max_length=50)
    image=models.ImageField(blank=True,verbose_name='Avatar',upload_to="uploads/" )
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    # tags = models.ForeignKey(Tag)
    tags=models.ManyToManyField(Tag, null=True )

    def __str__(self):
        return 'Question: {}'.format(self.head)
    def total_ans(self):
        """
        Likes for the company
        :return: Integer: Likes for the company
        """

        return  Answer.objects.filter(post=self).count()



    def total_likes(self):
        """
        Likes for the company
        :return: Integer: Likes for the company
        """
        rate=0
        likes= Like.objects.filter(post=self)
        for i in likes:
            if i.rate==True:
                rate+=1
            else:
                rate-=1
        return  rate



class Answer(models.Model):
    post=models.ForeignKey(Question)
    text=models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    user=models.ForeignKey(Author)

    def __str__(self):
        return 'Answer: {}'.format(self.post.pk)



class Like(models.Model):
    user=models.ForeignKey(Author)
    post=models.ForeignKey(Question,unique=False)
    rate=models.BooleanField()
    class Meta:
        unique_together=['user','post']
    def __str__(self):
        return 'Like from: {}'.format(self.user.nickname)