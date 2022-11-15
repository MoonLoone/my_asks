from django.contrib import admin
from myapp.models import Answer
from myapp.models import Ask
from myapp.models import Tag
from myapp.models import Like
from myapp.models import FoxUser

admin.site.register(Answer)
admin.site.register(Ask)
admin.site.register(Tag)
admin.site.register(Like)
admin.site.register(FoxUser)


