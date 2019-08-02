from datetime import datetime

from django.db.models import Q, Count, Avg
from pytz import UTC

from db.models import User, Blog, Topic


def create():
    # Создать пользователя first_name = u1, last_name = u1.
    user1 = User()
    user1.first_name, user1.last_name = "u1", "u1"
    user1.save()

    # Создать пользователя first_name = u2, last_name = u2.
    user2 = User()
    user2.first_name, user2.last_name = "u2", "u2"
    user2.save()

    # Создать пользователя first_name = u3, last_name = u3.
    user3 = User()
    user3.first_name, user3.last_name = "u3", "u3"
    user3.save()

    # Создать блог title = blog1, author = u1.
    blog1 = Blog()
    blog1.tittle = "blog1"
    blog1.author = user1
    blog1.save()

    # Создать блог title = blog2, author = u1.
    blog2 = Blog()
    blog2.tittle = "blog2"
    blog2.author = user1
    blog2.save()

    # Подписать пользователей u1 u2 на blog1, u2 на blog2.

    # Создать топик title = topic1, blog = blog1, author = u1.

    # Создать топик title = topic2_content, blog = blog1, author = u3, created = 2017-01-01.

    # Лайкнуть topic1 пользователями u1, u2, u3.


def edit_all():
    """Поменять first_name на uu1 у всех пользователей (функция edit_all)."""
    pass


def edit_u1_u2():
    """Поменять first_name на uu1 у пользователей, у которых first_name u1 или u2 (функция edit_u1_u2)."""
    pass


def delete_u1():
    """Удалить пользователя с first_name u1 (функция delete_u1)."""
    pass


def unsubscribe_u2_from_blogs():
    """Отписать пользователя с first_name u2 от блогов (функция unsubscribe_u2_from_blogs)."""
    pass


def get_topic_created_grated():
    """Найти топики у которых дата создания больше 2018-01-01"""
    pass


def get_topic_title_ended():
    """Найти топик у которого title заканчивается на content"""
    pass


def get_user_with_limit():
    """Получить 2х первых пользователей (сортировка в обратном порядке по id)"""
    pass


def get_topic_count():
    """Получить количество топиков в каждом блоге, назвать поле topic_count,
    отсортировать по topic_count по возрастанию"""
    pass


def get_avg_topic_count():
    """Получить среднее количество топиков в блоге"""
    pass


def get_blog_that_have_more_than_one_topic():
    """Найти блоги, в которых топиков больше одного"""
    pass


def get_topic_by_u1():
    """Получить все топики автора с first_name u1"""
    pass


def get_user_that_dont_have_blog():
    """Найти пользователей, у которых нет блогов, отсортировать по возрастанию id"""
    pass


def get_topic_that_like_all_users():
    """Найти топик, который лайкнули все пользователи"""
    pass


def get_topic_that_dont_have_like():
    """Найти топики, у которы нет лайков"""
    pass
