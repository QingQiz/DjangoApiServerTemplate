#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .apis import *
from django.urls import path


urlpatterns = [
    path('newKey', newKey),
    path('keyInfo', getKeyInfo),
]
