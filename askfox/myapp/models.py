import datetime

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Count


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class FoxUser(User):
    image = models.ImageField(default='askfox/static/img/default_user.png', blank=True)


def __str__(self):
    return self.name


class Like(models.Model):
    ask_parent = models.ForeignKey('Ask', on_delete=models.CASCADE, null=True, blank=True)
    answer_parent = models.ForeignKey('Answer', on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(FoxUser, on_delete=models.CASCADE)


class Answer(models.Model):
    title = models.CharField(max_length=100, default="Default title")
    content = models.TextField(
        default="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
    is_correct = models.BooleanField(default=False)
    ask_parent = models.ForeignKey('Ask', on_delete=models.CASCADE)
    user = models.ForeignKey(FoxUser, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.title


class AskManager(models.Manager):
    def get_best_ask(self):
        return super().get_queryset().annotate(number_of_like=Count('like')).order_by('-number_of_like').all()

    def get_ask_by_tag(self, tag_name):
        return super().get_queryset().filter(tags__name=tag_name).annotate(number_of_like=Count('like')).order_by(
            '-number_of_like').order_by('is_correct').all()

    def get_all_asks_by_date(self):
        return super().get_queryset().order_by('date').all()

    def get_answers_for_ask(self, searching_ask_id):
        return Answer.objects.get_queryset().filter(ask_parent_id=searching_ask_id).annotate(number_of_like=Count('like')).order_by(
            '-number_of_like').all()


class Ask(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(
        default="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
    tags = models.ManyToManyField(Tag)
    user = models.ForeignKey(FoxUser, on_delete=models.CASCADE, blank=True)
    date = models.DateField(default=datetime.datetime(2022, 11, 13, 19, 23, 1, 0))
    objects = AskManager()

    def __str__(self):
        return self.title
