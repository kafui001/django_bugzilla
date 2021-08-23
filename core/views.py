from django.contrib.auth import authenticate,login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView, DetailView, UpdateView, DeleteView,View

from .mixins import SigninRequiredMixin,SubmitterNotAllowedMixin
from .models import BugUser, Task,Notification,Developer
from .forms import TaskForm, TaskEditForm

#Create your views here.

class TaskView(SigninRequiredMixin,SubmitterNotAllowedMixin,FormView):
    model = Task
    template_name = 'core/task.html'
    form_class = TaskForm
    success_url = reverse_lazy('core:task')

    def get_context_data(self, **kwargs):
        context = super(TaskView, self).get_context_data(**kwargs)
        context['tasks']        = Task.objects.all()
        context['unassigned']   = Task.objects.filter(status='open')
        context['in_progress']  = Task.objects.filter(status='in progress')
        context['needs_review'] = Task.objects.filter(status='review')
        context['completed']    = Task.objects.filter(status='completed')
        return context

#     # limit task creation to only admin and project manager
    def form_valid(self, form):
        form = form.save(commit=False)
        if self.request.user.is_project_manager or self.request.user.is_superuser:
            form.creator = self.request.user
            form.status = 'open'
            form.save()

            return super(TaskView, self).form_valid(form)
        else:
            print("you are not authorized to create a task")
#             # fix this section

        


class TaskDetailView(SigninRequiredMixin,SubmitterNotAllowedMixin,DetailView):
    model               = Task
    context_object_name = 'task'
    template_name       = 'core/task_detail.html'

    def get_context_data(self, **kwargs):
        context                 = super(TaskDetailView, self).get_context_data(**kwargs)
        context['assign_dev']   = Developer.objects.all()
        return context


class AssignTaskView(View):
   
    def post(self, request, *args,**kwargs):
        if self.request.POST['dev'] != 'none':
            task_id = self.kwargs['pk']
            dev_id = self.request.POST['dev']
            
            dev = Developer.objects.get(id=dev_id)
            

            task_instance = Task.objects.get(id=task_id)
            task_instance.developer_assigned = dev
            task_instance.save(update_fields=['developer_assigned'])

            Notification.objects.create(
                notification_type = 8,
                to_user           = dev.username,
                from_user         = self.request.user,
                task            = task_instance
            )
    
            return redirect(reverse('core:task_detail', kwargs={'pk': self.kwargs['pk']}))




class TaskEditView(SigninRequiredMixin,SubmitterNotAllowedMixin,UpdateView):
    model = Task
    form_class = TaskEditForm
    template_name = 'core/task_edit.html'
    
    def get_success_url(self):
        return reverse_lazy('core:task_detail', kwargs={'pk': self.kwargs['pk']})


class TaskDeleteView(SigninRequiredMixin,SubmitterNotAllowedMixin,DeleteView):
    model = Task
    context_object_name = 'task'
    template_name = 'core/task_delete.html'
    success_url = reverse_lazy('core:task')



class AssignTaskToView(SigninRequiredMixin,SubmitterNotAllowedMixin,DetailView):
    model               = Task
    context_object_name = 'task'
    template_name       = 'core/task_assigned_to.html'



class DeleteNotification(DeleteView):
    model = Notification

    def post(self, request, pk,*args,**kwargs):

        notification = Notification.objects.get(id=pk)
        if notification.notification_type == 1:
            tic_id = notification.ticket.id
            notification.delete()

            return redirect(reverse('ticket:ticket_detail', kwargs={'pk': tic_id}))
        elif notification.notification_type == 3:
            proj_id = notification.project.id
            notification.delete()

            return redirect(reverse('project:project_detail', kwargs={'pk': proj_id}))    
        elif notification.notification_type == 4:
            dev_role = notification.dev_role_assign.id
            notification.delete()
            return redirect('assign_dev_role')
        elif notification.notification_type == 5:
            notification.delete()
            
            return redirect('assign_pm_role')
        elif notification.notification_type == 6:
            notification.delete()
           
            return redirect('assign_admin_role')
        elif notification.notification_type == 7:
            tic_id = notification.ticket.id
            notification.delete()
            
            # return redirect('assigned_role', kwargs={'pk': tic_id})
            return redirect(reverse('ticket:assigned_to', kwargs={'pk': tic_id}))
        elif notification.notification_type == 8:
            task_id = notification.task.id
            notification.delete()
          
            # return redirect('assigned_role', kwargs={'pk': tic_id})
            return redirect(reverse('core:task_assigned_to', kwargs={'pk': task_id}))
        elif notification.notification_type == 9:
            notification.delete()
            
            return redirect('project_pm_role')

##  DEMO LOGIN CLASSES

class AdminDemoLoginView(View):
    def post(self, request, *args, **kwargs):
       
        admin = BugUser.objects.get(username='admin')
        admin_password = 'smile'
        authenticate(username=admin, password=admin_password)
        login(request,admin )
        return redirect('project:project_home')


class DeveloperDemoLoginView(View):
    def post(self, request, *args, **kwargs):
       
        developer = BugUser.objects.get(username='developer')
        dev_password = 'testing1234'
        authenticate(username=developer, password=dev_password)
        login(request,developer )
        return redirect('project:project_home')


class PmDemoLoginView(View):
    def post(self, request, *args, **kwargs):
        pm = BugUser.objects.get(username='projectManager')
        pm_password = 'testing1234'
        authenticate(username=pm, password=pm_password)
        login(request,pm )
        return redirect('project:project_home')


class SubmitterDemoLoginView(View):
    def post(self, request, *args, **kwargs):
        submitter = BugUser.objects.get(username='submitter')
        submitter_password = 'testing1234'
        authenticate(username=submitter, password=submitter_password)
        login(request,submitter )
        return redirect('ticket:ticket_home')