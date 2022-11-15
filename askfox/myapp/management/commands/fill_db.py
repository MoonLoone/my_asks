import random
from abc import ABC

from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

from myapp import models

from myapp import utils


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('ratio', type=int)

    def handle(self, *args, **kwargs):
        ratio = kwargs['ratio']
        tags_list = []
        ordinary_tag_list = []
        for i in range(10):
            ordinary_tag_list.append(f'tag {i}')
        for i in range(ratio):
            user = models.FoxUser()
            user.password = get_random_string(10)
            user.username = get_random_string(7)
            user.save()
            tag = models.Tag()
            tag.name = f"{get_random_string(5)}"
            tag.save()
            for k in range(10):
                ask = models.Ask()
                ask.user = user
                ask.title = f"Title {get_random_string(20)}"
                ask.content = get_random_string(50)
                ask.save()
                ask.tags.add(tag)
                tag2 = models.Tag()
                tag2.name = random.choice(ordinary_tag_list)
                tag2.save()
                ask.tags.add(tag2)
                tag2 = models.Tag()
                tag2.name = random.choice(ordinary_tag_list)
                tag2.save()
                ask.tags.add(tag2)
                for j in range(10):
                    answer = models.Answer()
                    answer.user = user
                    answer.content = get_random_string(15)
                    answer.title = f"Answer title {j * k * i+1}"
                    answer.save()
                    for h in range(2):
                        like = models.Like()
                        like.type = random.choice(utils.LIKE_TYPES)[1]
                        like.user = user
                        like.save()
                        if like.type == utils.LIKE_TYPES[1][1]:
                            ask.likes.add(like)
                        else:
                            answer.likes.add(like)
                    answer.save()
                    ask.answers.add(answer)
                ask.save()
        models.Tag.objects.bulk_create(tags_list)
