from django.db import models
from django.contrib.auth.models import User,Group,Permission

class Student(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    code = models.CharField(max_length=15)
    def save(self, *args, **kwargs):
        user = User(
            is_superuser=False,
            username= self.name,
            first_name = self.name,
            last_name = self.last_name,
            is_staff=True,
            is_active=True,
        )
        user.set_password(self.code)
        user.save()
        try:
            group = Group.objects.get(name='student')
        except Group.DoesNotExist:
            group = Group.objects.create(name='student')
            view_answer_permission = Permission.objects.get(codename='view_answer')
            group.permissions.add(view_answer_permission)
        user.groups.add(group)
        super(Student,self).save() 
    def __str__(self):
        return self.name


class Test(models.Model):
    name = models.CharField(max_length=255) 
    def __str__(self):
        return self.name

class Question(models.Model):
    test = models.ForeignKey(Test,related_name='questions', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    answer_correct = models.CharField(max_length=255)
    points = models.IntegerField() 
    def __str__(self):
        return '%s : %s'%(str(self.test),self.name) 

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question,related_name='answers', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    points = models.IntegerField(default=0)
    def save(self, *args, **kwargs):
        if self.question.answer_correct == self.name:
            self.is_correct = True
            self.points = self.question.points
        super(Answer,self).save()     
    def __str__(self):
        return str(self.question)
