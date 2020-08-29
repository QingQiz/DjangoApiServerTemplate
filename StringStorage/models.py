#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import common.models as m

from django.db import models


class ApiKey(models.Model):
    name = models.CharField(max_length=50)


class StringStorage(models.Model):
    apiKey = models.ForeignKey(m.ApiKey, on_delete=models.CASCADE)
    name = models.CharField(max_length=256, null=False)
    value = models.TextField(default='')
