from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import BaseRegisterForm
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

from newsapp.models import Post

from newsapp.filters import NewsFilter

from newsapp.models import Comments

from newsapp.filters import CommentsFilter


class CommentsList(ListView):
    model = Comments
    ordering = ['-time_in']
    template_name = 'sign/comments.html'
    context_object_name = 'comments'
    paginate_by = 10

    def get_queryset(self):
        return Comments.objects.filter(author_id=self.request.user.id).distinct()


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'


@login_required
def upgrade_me(request):
    user = request.user
    premium_group = Group.objects.get(name='Authors')
    if not request.user.groups.filter(name='Authors').exists():
        premium_group.user_set.add(user)
    return redirect('/')


def delete_comment(request):
    comment = Comments.objects.get(id=request.POST['id_cat'])
    comment.delete()
    return redirect('/')


def approve_comment(request):
    comment = Comments.objects.get(id=request.POST['id_cat'])
    subject = f'{comment.author.email} утвердил ваш комментарий'

    send_mail(
        subject=subject,
        message=comment.comment_text,
        from_email='gtna8e6@yandex.ru',
        recipient_list=[comment.user],
        fail_silently=False
    )
    return redirect('/')
