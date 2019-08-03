from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.http import require_GET, require_POST
from db import query
# from grader.db import query


@require_GET
def create(request):
    query.create()
    return HttpResponse()


@require_GET
def edit_all(request):
    """Поменять first_name на uu1 у всех пользователей"""
    return HttpResponse(query.edit_all())


@require_GET
def edit_u1_u2(request):
    """Поменять first_name на uu1 у пользователей, у которых first_name u1 или u2"""
    return HttpResponse(query.edit_u1_u2())


@require_GET
def delete_u1(request):
    """Удалить пользователя с first_name u1"""
    return HttpResponse(query.delete_u1())


@require_GET
def unsubscribe_u2_from_blogs(request):
    """Отписать пользователя с first_name u2 от блогов (функция unsubscribe_u2_from_blogs)."""
    query.unsubscribe_u2_from_blogs()
    return HttpResponse()


@require_GET
def get_topic_created_grated(request):
    """Найти топики у которых дата создания больше 2018-01-01"""
    return HttpResponse(query.get_topic_created_grated())


@require_GET
def get_topic_title_ended(request):
    """Найти топик у которого title заканчивается на content"""
    query.get_topic_title_ended()
    return HttpResponse()


@require_GET
def get_user_with_limit(request):
    """Получить 2х первых пользователей (сортировка в обратном порядке по id)"""
    query.get_user_with_limit()
    return HttpResponse()


@require_GET
def get_topic_count(request):
    """Получить количество топиков в каждом блоге, назвать поле topic_count,
    отсортировать по topic_count по возрастанию"""
    query.get_topic_count()
    return HttpResponse()


@require_GET
def get_avg_topic_count(request):
    """Получить среднее количество топиков в блоге"""
    query.get_avg_topic_count()
    return HttpResponse()


@require_GET
def get_blog_that_have_more_than_one_topic(request):
    """Найти блоги, в которых топиков больше одного"""
    query.get_blog_that_have_more_than_one_topic()
    return HttpResponse()


@require_GET
def get_topic_by_u1(request):
    """Получить все топики автора с first_name u1"""
    query.get_topic_by_u1()
    return HttpResponse()


@require_GET
def get_user_that_dont_have_blog(request):
    """Найти пользователей, у которых нет блогов, отсортировать по возрастанию id"""
    query.get_user_that_dont_have_blog()
    return HttpResponse()


@require_GET
def get_topic_that_like_all_users(request):
    """Найти топик, который лайкнули все пользователи"""
    query.get_topic_that_like_all_users()
    return HttpResponse()


@require_GET
def get_topic_that_dont_have_like(request):
    """Найти топики, у которы нет лайков"""
    query.get_topic_that_dont_have_like()
    return HttpResponse()
