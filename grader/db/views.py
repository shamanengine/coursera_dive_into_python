from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.http import require_GET, require_POST
from db import query


@require_GET
def create(request):
    query.create()
    return HttpResponse()
