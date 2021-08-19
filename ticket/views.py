import random

from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView,FormView, DetailView, UpdateView, DeleteView,View

from .forms import TicketForm, TicketEditForm, CommentForm
from core.models import Ticket, Developer, AllImage, Comment,Notification,Administrator
from core.mixins import SigninRequiredMixin,SubmitterNotAllowedMixin,SubmitterAndDevNotAllowedMixin


# Create your views here.

class TicketHomeView(SigninRequiredMixin,ListView):
    model               = Ticket
    template_name       = 'ticket/ticket.html'
    context_object_name = 'tickets'
    ordering            = ['-date_created']
    paginate_by         = 6

    def get_context_data(self, **kwargs):
        context         = super(TicketHomeView, self).get_context_data(**kwargs)
        context['form'] = TicketForm()
        return context

# 'POST' info from ticket creation form from ticket.html
class TicketFormView(FormView):
    model       = Ticket
    form_class  = TicketForm
    success_url = reverse_lazy('ticket:ticket_home')

    def form_valid(self, form):
        form         = TicketForm(self.request.POST)
        new_image    = self.request.FILES.get('image') 

        form         = form.save(commit=False)
        form.creator = self.request.user
        form.status  = 'open'

        # create a ticket number for each ticket instance
        while True:
            id = random.randint(10000,99999)
            if Ticket.objects.filter(ticket_id=id).count() == 0:
                break 
        form.ticket_id = id 
        form.save()
        
        if new_image != None:
            save_new_image = AllImage.objects.create(
                ticket = form,
                image = new_image
            )


        administrators = Administrator.objects.all()

        # loop through administrators to create notification for each admin about 
        # new ticket instance creation
        for admin in administrators:
            Notification.objects.create(
                notification_type = 1,
                to_user           = admin.username,
                from_user         = self.request.user,
                ticket            = form
            )

        return super(TicketFormView, self).form_valid(form)
 
class TicketDetailView(SigninRequiredMixin,SubmitterNotAllowedMixin,DetailView):
    model               = Ticket
    form_class          = TicketForm
    template_name       = 'ticket/ticket_detail.html'
    context_object_name = 'ticket'
    

    def get_context_data(self, **kwargs):
        context = super(TicketDetailView, self).get_context_data(**kwargs)
        
        context['comment_form'] = CommentForm
        context['image']        = AllImage.objects.all()
        context['all_comments'] = Comment.objects.all()
        context['assign_dev']   = Developer.objects.all()
        return context

 
 
# submitted comment from ticket_detail.html
class CommentFormWork(CreateView):
    model       = Comment
    form_class  = CommentForm
    
    def get_success_url(self):
        return reverse_lazy('ticket:ticket_detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.ticket_id = self.kwargs['pk']
        
        return super().form_valid(form)
       

class AssignTicketView(SigninRequiredMixin,View):
   
    def post(self, request, *args,**kwargs):
        if self.request.POST['dev'] != 'none':
            ticket_id = self.kwargs['pk']
            dev_id = self.request.POST['dev']
            
            dev = Developer.objects.get(id=dev_id)
            

            ticket_instance = Ticket.objects.get(id=ticket_id)
            ticket_instance.assigned_to = dev
            ticket_instance.save(update_fields=['assigned_to'])

            Notification.objects.create(
                notification_type = 7,
                to_user           = dev.username,
                from_user         = self.request.user,
                ticket            = ticket_instance
            )
    
            return redirect(reverse('ticket:ticket_detail', kwargs={'pk': self.kwargs['pk']}))
            

class AssignToView(SigninRequiredMixin,DetailView):
    model               = Ticket
    context_object_name = 'ticket'
    template_name       = 'ticket/assigned_to.html'
    



class TicketEditView(SigninRequiredMixin,SubmitterAndDevNotAllowedMixin,UpdateView):
    model         = Ticket
    form_class    = TicketEditForm
    template_name = 'ticket/ticket_edit.html'

    def get_success_url(self):
        return reverse_lazy('ticket:ticket_detail', kwargs={'pk': self.kwargs['pk']})



class TicketDeleteView(SigninRequiredMixin,SubmitterAndDevNotAllowedMixin,DeleteView):
    model               = Ticket
    context_object_name = 'ticket'
    template_name       = 'ticket/ticket_delete.html'
    success_url         = reverse_lazy('ticket:ticket_home')

