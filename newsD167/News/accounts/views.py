from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import Category, Comments, Post
from News.newsapp.filters import CommentsFilter, NewsFilter


class IndexView(LoginRequiredMixin, TemplateView, ListView):
    model = Comments
    ordering = ['-time_in']
    template_name = 'protect/index.html'
    context_object_name = 'comments'
    paginate_by = 10

    def get_object(self, **kwargs):
        return self.request.user

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context['is_not_Authors'] = not self.request.user.groups.filter(name='Authors').exists()
        context['category'] = Category.objects.all()
        user_cat = list()
        for u in Category.objects.all():
            print(u)
        context['user_category'] = user_cat
        return context
