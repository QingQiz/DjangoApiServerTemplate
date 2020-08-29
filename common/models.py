import random
import string

from django.db import models


def getDefaultValue():
    generator = string.ascii_letters + string.digits

    return ''.join(random.choices(generator, k=256))


class ApiKey(models.Model):
    name = models.CharField(max_length=128, default='')
    description = models.TextField(default='')
    value = models.TextField(default=getDefaultValue, primary_key=True)
    createTime = models.DateTimeField(auto_now=True)
