# @Time : 2020/6/21 18:57
# @Author : Chenguangfu
# @Site : 
# @File : urls.py
# @Software: PyCharm

from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),

    # ex: /polls/5/
    # 加上specifics路由
    # path('specifics/<int:question_id>/', views.detail, name='detail'),
    # 注释，修改为带有具体指向的命名空间
    path('<int:question_id>/', views.detail, name='detail'),

    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),

    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

]