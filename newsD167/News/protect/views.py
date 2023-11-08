from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from newsapp.models import Category


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'protect/index.html'

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
            if u.subscribers.filter(id=user.id).exists():
                user_cat.append(u)
        context['user_category'] = user_cat
        return context
