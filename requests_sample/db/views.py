from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.http import require_GET, require_POST
from grader.db.query import create


@require_GET
def create():
    create()
    return HttpResponse()
