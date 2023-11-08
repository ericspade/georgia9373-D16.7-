from django import forms
from .models import Post, Comments
from django.utils.translation import ugettext_lazy as _


class NewsForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'header',
            'author',
            'category',
            'article_text',
        ]


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'header',
            'author',
            'category',
            'article_text',
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = [
            'user',
            'author',
            'comment_text',
            'rating',
        ]
        labels = {
            'user': _('Email'),
        }

        def __init__(self, *args, **kwargs):
            self.user.label = "Email"
            super(CommentForm, self).__init__(*args, **kwargs)
