from celery import shared_task
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string


@shared_task
def notify_subscribers_news_createdtask(instance, action):
    from .models import Post
    instance = Post.objects.get(pk=instance)
    subject = f'{instance.header} {instance.article_text}'
    if action == 'post_add':
        if instance.type == 0:
            for cat in instance.category.all():
                print(cat)
                for sub in User.objects.filter(subscribers__category=cat):
                    print(sub)
                    send_mail(
                        subject=subject,
                        message=instance.article_text,
                        from_email='',
                        recipient_list=[sub.email],
                        fail_silently=False,
                        html_message=render_to_string("newsemail.html", {'post': instance})
                    )
        else:
            send_mail(
                subject=subject,
                message=instance.article_text,
                from_email='',
                recipient_list=['gtna8e6@gmail.com'],
                fail_silently=False
            )


@shared_task
def weekly_news():
    from .models import Category
    from .models import Post
    for cat in Category.objects.all():
        print(cat)
        for sub in User.objects.filter(subscribers__category=cat):
            print(sub)
            entries = Post.objects.filter(category=cat)
            send_mail(
                subject='Weekly news',
                message='',
                from_email='',
                recipient_list=[sub.email],
                fail_silently=False,
                html_message=render_to_string("newsweekly.html", {'entries': entries})
            )
