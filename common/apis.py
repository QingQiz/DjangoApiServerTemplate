#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from .models import ApiKey

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


def retJson(obj=None, **kwargs):
    return HttpResponse(json.dumps(kwargs if obj is None else obj), content_type='application/json')


@csrf_exempt
def newKey(request):
    """
    @api {post} /common/newKey Create a new apiKey
    @apiVersion 1.0.0

    @apiDescription create a new apiKey

    @apiName newKey
    @apiGroup common

    @apiParam {string} name Key name
    @apiParam {string} [description] Key description

    @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
        {
            "error": 0,
            "result": {
                "value": "apiKey here"
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
    description = request.POST.get('description')
    description = description if description else ''

    if name is None:
        return retJson(error=1, reason='need: name')

    if ApiKey.objects.filter(name=name).exists():
        return retJson(error=1, reason='exists')

    key = ApiKey(name=name, description=description)
    key.save()

    return retJson(error=0, result={'value': key.value})


@csrf_exempt
def getKeyInfo(request):
    """
    @api {post} /common/keyInfo apiKey info
    @apiVersion 1.0.0

    @apiDescription Get apiKey info

    @apiName keyInfo
    @apiGroup common

    @apiParam {string} key apiKey

    @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
        {
            "error": 0,
            "result": {
                "name": "key name",
                "description": "key description"
            }
        }
    @apiErrorExample {json} Error-Response:
        HTTP/1.1 200 OK
        {
            "error": 1,
            "reason": "error reason here"
        }
    """
    value = request.POST.get('key')

    if value is None:
        return retJson(error=1, reason='need: key')

    que = ApiKey.objects.filter(value=value)

    if que.exists():
        key = que[0]
        return retJson(error=0, result={'name': key.name, 'description': key.description})

    return retJson(error=1, reason='not found')
