import django_filters
from django.forms import DateInput
from django_filters import FilterSet
from .models import Post, Comments


class NewsFilter(FilterSet):
    header = django_filters.CharFilter(lookup_expr='icontains', label='Заголовок содержит:')
    release_year = django_filters.NumberFilter(field_name='time_in', lookup_expr='year__gt', label='Позже какого года?')

    class Meta:
        model = Post
        fields = ['header', 'category']


class CommentsFilter(FilterSet):
    comment_text = django_filters.CharFilter(lookup_expr='icontains', label='Комментарий содержит:')
    release_year = django_filters.NumberFilter(field_name='time_in', lookup_expr='year__gt', label='Позже какого года?')

    class Meta:
        model = Comments
        fields = ['comment_text']
