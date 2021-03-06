import datetime

from django import template
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple, FileInput, ClearableFileInput
from django.utils import timezone
from .jdate_tags import farsi_digits

register = template.Library()


@register.filter()
def is_radio_select(instance):
    return type(instance) == RadioSelect


@register.filter()
def is_multiple_checkbox(instance):
    return type(instance) == CheckboxSelectMultiple


@register.filter()
def is_file_input(instance):
    return type(instance) == FileInput or type(instance) == ClearableFileInput


@register.filter()
def get_post_real_url(post):
    return post.get_absolute_url


@register.filter()
def post_is_new(post):
    return post.publish_date > timezone.now() - datetime.timedelta(days=7)


@register.filter()
def get_persian_comma_separated_money(number):
    return farsi_digits(format(number, ','))


@register.filter()
def log(object):
    print(object)
    return ''
