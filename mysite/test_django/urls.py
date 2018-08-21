from django.urls import path

from . import views

app_name = 'test_django'
urlpatterns = [
    # ex: /test_django/
    path('', views.index, name='index'),
    # ex: /test_django/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /test_django/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /test_django/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]