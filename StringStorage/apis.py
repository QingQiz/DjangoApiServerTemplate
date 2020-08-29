#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from .models import StringStorage
from common.models import ApiKey

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


def retJson(obj=None, **kwargs):
    return HttpResponse(json.dumps(kwargs if obj is None else obj), content_type='application/json')

@csrf_exempt
def update(request):
    """
    @api {post} /string/update update a string
    @apiVersion 1.0.0

    @apiDescription update a string

    @apiName updateString
    @apiGroup string

    @apiParam {string} name string name
    @apiParam {string} key apiKey
    @apiParam {string} value string value

    @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
        {
            "error": 0,
            "result": {
                "update": 0,
                "create": 1
            }
        }
    @apiErrorExample {json} Error-Response:
        HTTP/1.1 200 OK
        {
            "error": 1,
            "reason": "error reason here"
        }
    """
    name = request.POST.get('name')
    value = request.POST.get('value')
    key = request.POST.get('key')

    if name is None:
        return retJson(error=1, reason='need: name')
    if key is None:
        return retJson(error=1, reason='need: key')
    if value is None:
        return retJson(error=1, reason='need: value')

    key = ApiKey.objects.filter(value=key)
    if not key.exists():
        return retJson(error=1, reason='key not found')
    key = key[0]

    ss = StringStorage.objects.filter(name=name, apiKey=key)
    if ss.exists():
        ss = ss[0]

        ss.value = value
        ss.save()

        return retJson(error=0, result={'update': 1, 'create': 0})

    ss = StringStorage(name=name, value=value, apiKey=key)
    ss.save()
    return retJson(error=0, result={'update': 0, 'create': 1})


@csrf_exempt
def getInfo(request):
    """
    @api {post} /string/get get a string
    @apiVersion 1.0.0

    @apiDescription get a string

    @apiName getString
    @apiGroup string

    @apiParam {string} name string name
    @apiParam {string} key apiKey

    @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
        {
            "error": 0,
            "result": {
                "update": 0,
                "create": 1
            }
        }
    @apiErrorExample {json} Error-Response:
        HTTP/1.1 200 OK
        {
            "error": 1,
            "reason": {
                "name": "string name",
                "value": "string value"
            }
        }
    """
    name = request.POST.get('name')
    key = request.POST.get('key')

    if name is None:
        return retJson(error=1, reason='need: name')
    if key is None:
        return retJson(error=1, reason='need: key')

    key = ApiKey.objects.filter(value=key)
    if not key.exists():
        return retJson(error=1, reason='key not found')
    key = key[0]

    ss = StringStorage.objects.filter(name=name, apiKey=key)

    if ss.exists():
        ss = ss[0]
        return retJson(error=0, result={'name': ss.name, 'value': ss.value})

    return retJson(error=1, reason='not found')
