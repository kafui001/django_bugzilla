import random

from django.utils import timezone
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save


# Create your models here.
class BugUser(AbstractUser):
    is_developer       = models.BooleanField(default=False)
    is_project_manager = models.BooleanField(default=False)

 
# class UserProfile(models.Model):
#     user = models.OneToOneField(BugUser, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.user.username



# def create_userprofile_signal(sender,instance,created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)


# post_save.connect(create_userprofile_signal, sender=UserProfile)


class Administrator(models.Model):
    username = models.OneToOneField(BugUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.username.username

    

class ProjectManager(models.Model):
    username  = models.OneToOneField(BugUser, on_delete=models.CASCADE)
    admin =  models.ForeignKey(Administrator,on_delete=models.SET_NULL, null=True,related_name='pm_assigner')

    def __str__(self):
        return self.username.username

    


class Developer(models.Model):
    username              = models.OneToOneField(BugUser, on_delete=models.CASCADE)
    assigner          = models.ForeignKey(BugUser,on_delete=models.SET_NULL, null=True,related_name='dev_assigner')
    

    def __str__(self):
        return self.username.username

class Task(models.Model):
    title              = models.CharField(max_length=255)
    description        = models.TextField()
    creator            = models.ForeignKey(BugUser,on_delete=models.SET_NULL, null=True,related_name='task_author')
    developer_assigned = models.ForeignKey(Developer,on_delete=models.SET_NULL, null=True,blank=True,related_name='task_developer')
    date_created       = models.DateField(auto_now_add=True)
    date_assigned      = models.DateField(auto_now=True)
    date_completed     = models.DateField(auto_now=True)
    status             = models.CharField(max_length=255)
    priority           = models.CharField(max_length=255)
    project            = models.ForeignKey('Project',on_delete=models.SET_NULL, null=True,blank=True,related_name='task_project')
    
    def __str__(self):
        return self.title

class TaskPriority(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class TaskStatus(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class ProjectStatus(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Project(models.Model):
    title        = models.CharField(max_length=255)
    description  = models.TextField()
    creator      = models.ForeignKey(Administrator,on_delete=models.SET_NULL, null=True,blank=True,related_name='project_creator')
    status       = models.CharField(max_length=50)
    date_created = models.DateField(auto_now_add=True)
    begin_date   = models.DateField(null=True, blank=True)
    end_date     = models.DateField(null=True, blank=True)
    project_lead = models.ForeignKey(ProjectManager,on_delete=models.SET_NULL, null=True,blank=True,related_name='project_pm')
    completion   = models.CharField(max_length=255)


    def __str__(self):
        return self.title
        


class Ticket(models.Model):
    ticket_id          = models.CharField(max_length=6, default='', unique=True)
    title              = models.CharField(max_length=150)
    description        = models.TextField()
    creator            = models.ForeignKey(BugUser,on_delete=models.SET_NULL, null=True,related_name='ticket_author')
    assigned_to        = models.ForeignKey(Developer,on_delete=models.SET_NULL, null=True,blank=True,related_name='ticket_developer')
    priority           = models.CharField(max_length=50)
    status             = models.CharField(max_length=50)
    project            = models.ForeignKey('Project',on_delete=models.SET_NULL, null=True,blank=True,related_name='ticket_project')
    date_created       = models.DateField(auto_now_add=True)
    date_resolved      = models.DateField(auto_now=True)
                 
    def __str__(self):
        return self.title

class AllImage(models.Model):
    ticket = models.ForeignKey(Ticket, related_name='img_ticket', on_delete=models.CASCADE,null=True)
    image  = models.ImageField(null=True, blank=True)


class Comment(models.Model):
    ticket = models.ForeignKey(Ticket,related_name='ticket_comment',on_delete=models.CASCADE,null=True)
    author = models.ForeignKey(BugUser,related_name='comment_author',on_delete=models.CASCADE,null=True)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[:10]


class Notification(models.Model):
    # 1=ticket 2=task 3=project 4=dev_role 5=pm_role 6=admin_role 7=assigned_ticket 8=assigned_task 9=assigned_project
    notification_type    = models.IntegerField()
    to_user              = models.ForeignKey(BugUser, related_name='notification_to',on_delete=models.CASCADE)  
    from_user            = models.ForeignKey(BugUser, related_name='notification_from',on_delete=models.CASCADE)     
    notification_is_seen = models.BooleanField(default=False)
    date_created         = models.DateField(default=timezone.now)
    project              = models.ForeignKey('Project',on_delete=models.SET_NULL,related_name='+',null=True, blank=True)
    task                 = models.ForeignKey(Task,on_delete=models.CASCADE, related_name='+',null=True, blank=True)
    ticket               = models.ForeignKey(Ticket,on_delete=models.CASCADE, related_name='+',null=True, blank=True)
    dev_role_assign      = models.ForeignKey(Developer,on_delete=models.CASCADE, related_name='+',null=True, blank=True)
    pm_role_assign       = models.ForeignKey(ProjectManager,on_delete=models.CASCADE, related_name='+',null=True, blank=True)
    admin_role_assign    = models.ForeignKey(Administrator,on_delete=models.CASCADE, related_name='+',null=True, blank=True)
    