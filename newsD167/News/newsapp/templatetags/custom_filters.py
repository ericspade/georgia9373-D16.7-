from django import template
import re

register = template.Library()

WORDS = ['урод', 'козел', 'гнида']


@register.filter()
def matyugi(text):
    for word in text.split():
        for mat in WORDS:
            if mat == word:
                word = "*"
    return text

