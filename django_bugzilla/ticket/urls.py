from django.urls import path
from django.views.decorators.http import require_POST
from .views import TicketHomeView, TicketFormView, TicketDetailView, TicketEditView, TicketDeleteView,CommentFormWork,AssignTicketView, AssignToView
# from .views import TicketHomeView, TicketFormView, TicketEditView, TicketDeleteView,ticket_detail_view
app_name = 'ticket'

urlpatterns = [
    path('',TicketHomeView.as_view(), name='ticket_home'),
    # path('detail/<int:pk>/',ticket_detail_view, name='ticket_detail'),
    path('detail/<int:pk>/',TicketDetailView.as_view(), name='ticket_detail'),
    path('edit/<int:pk>/',TicketEditView.as_view(), name='ticket_edit'),
    path('ticket/<int:pk>/',AssignTicketView.as_view(), name='ticket_response_form'),
    path('comment/<int:pk>/',CommentFormWork.as_view(), name='comment_form'),
    # path('comment/<int:id>',commentFormWork, name='comment_form'),
    path('delete/<int:pk>/',TicketDeleteView.as_view(), name='ticket_delete'),
    path('ticket_form/',TicketFormView.as_view(), name='ticket_form'),
    path('assigned_to/<int:pk>/',AssignToView.as_view(), name='assigned_to'),
]