#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .apis import *

from django.urls import path, include

urlpatterns = [
    path('update', update),
    path('get', getInfo)
]

