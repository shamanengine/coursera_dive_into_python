from datetime import datetime

from django.db.models import Q, Count, Avg
from pytz import UTC

from grader.db.models import User, Blog, Topic


def create():
    """
    Создать пользователя first_name = u1, last_name = u1.
    Создать пользователя first_name = u2, last_name = u2.
    Создать пользователя first_name = u3, last_name = u3.
    Создать блог title = blog1, author = u1.
    Создать блог title = blog2, author = u1.
    Подписать пользователей u1 u2 на blog1, u2 на blog2.
    Создать топик title = topic1, blog = blog1, author = u1.
    Создать топик title = topic2_content, blog = blog1, author = u3, created = 2017-01-01.
    Лайкнуть topic1 пользователями u1, u2, u3.
    """
    user1 = User()
    user1.first_name, user1.last_name = "u1", "u1"
    user1.save()


def edit_all():
    pass


def edit_u1_u2():
    pass


def delete_u1():
    pass


def unsubscribe_u2_from_blogs():
    pass


def get_topic_created_grated():
    pass


def get_topic_title_ended():
    pass


def get_user_with_limit():
    pass


def get_topic_count():
    pass


def get_avg_topic_count():
    pass


def get_blog_that_have_more_than_one_topic():
    pass


def get_topic_by_u1():
    pass


def get_user_that_dont_have_blog():
    pass


def get_topic_that_like_all_users():
    pass


def get_topic_that_dont_have_like():
    pass


if __name__ == "__main__":
    create()
