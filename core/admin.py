from django.contrib import admin
from .models import Notification, Task,BugUser,TaskStatus,TaskPriority,Comment,Ticket,AllImage, Administrator,ProjectManager,Developer,ProjectStatus,Project
# # Register your models here.

admin.site.register(BugUser)
admin.site.register(Task)
admin.site.register(TaskStatus)
admin.site.register(TaskPriority)
admin.site.register(Comment)
admin.site.register(Ticket)
admin.site.register(AllImage)
admin.site.register(Administrator)
admin.site.register(ProjectManager)
admin.site.register(Developer)
admin.site.register(Notification)
admin.site.register(ProjectStatus)
admin.site.register(Project)