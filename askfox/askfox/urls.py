from django.contrib import admin
from django.urls import path

from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('question/<int:question_id>', views.question, name='question'),
    path('login/', views.login, name='login'),
    path('ask/', views.ask, name='ask'),
    path('settings/', views.settings, name='settings'),
    path('signup/', views.signup, name='signup'),
    path('hot/', views.hot, name='hot'),
    path('tag/', views.tag, name='tag'),
]

handler404 = 'myapp.views.handler404'
