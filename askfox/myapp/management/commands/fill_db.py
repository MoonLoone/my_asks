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
        ordinary_tag_list = []
        for i in range(10):
            ordinary_tag_list.append(f'tag {i}')
        for i in range(ratio):
            tag = models.Tag()
            tag.name = get_random_string(5)
            tag.save()
            tag2 = models.Tag()
            tag2.name = random.choice(ordinary_tag_list)
            tag2.save()
            user = models.FoxUser()
            user.username = get_random_string(10)
            user.password = get_random_string(10)
            user.save()
            for j in range(10):
                ask = models.Ask()
                ask.title = get_random_string(15)
                ask.user = user
                ask.save()
                ask.tags.add(tag2)
                ask.tags.add(tag)
                for k in range(10):
                    answer = models.Answer()
                    answer.user = user
                    answer.title = f'title{i*j*k}'
                    answer.ask_parent = ask
                    answer.save()
                    for m in range(2):
                        like = models.Like()
                        like.user = user
                        if random.randint(1, 2) == 1:
                            like.ask_parent = ask
                        else:
                            like.answer_parent = answer
                        like.save()
