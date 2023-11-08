from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import BaseRegisterView, CommentsList, delete_comment, approve_comment
from .views import upgrade_me

urlpatterns = [
    path('login/',
         LoginView.as_view(template_name='sign/login.html'),
         name='login'),
    path('logout/',
         LogoutView.as_view(template_name='sign/logout.html'),
         name='logout'),
    path('signup/',
         BaseRegisterView.as_view(template_name='sign/signup.html'),
         name='signup'),
    path('comments/', CommentsList.as_view(template_name='sign/comments.html'), name='add_comment'),
    path('upgrade/', upgrade_me, name='upgrade'),
    path('comments/delete_comment/', delete_comment, name='delete_comment'),
    path('comments/approve_comment/', approve_comment, name='approve_comment'),
]
