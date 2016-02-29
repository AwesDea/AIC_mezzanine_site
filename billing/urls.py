# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns(
    'billing.views',
    url("^bankcb$", 'bank_callback', name='bank_callback'),
    url('^pay/$', 'payment', name='pay_site_price')
)
