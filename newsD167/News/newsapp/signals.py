from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

from .filters import NewsFilter
from .forms import NewsForm, ArticleForm
from .models import Post, Comments, User


@receiver(post_save, sender=Post)
def notify_news_created(sender, instance, created, **kwargs):
    if created:
        subject = f'{instance.header} {instance.article_text}'
    else:
        subject = f'Content changed for {instance.header} {instance.article_text}'

    send_mail(
        subject=subject,
        message=instance.article_text,
        from_email='gtna8e6@yandex.ru',
        recipient_list=['gtna8e6@gmail.com'],
        fail_silently=False
    )


@receiver(post_save, sender=Comments)
def notify_article_author_comment_created(instance, **kwargs):
    subject = f'{instance.user} оставил комментарий к вашему объявлению'

    send_mail(
        subject=subject,
        message=instance.comment_text,
        from_email='gtna8e6@yandex.ru',
        recipient_list=[instance.author.email],
        fail_silently=False
    )


