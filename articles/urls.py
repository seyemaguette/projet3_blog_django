from django.urls import path
from .views import home, details, list_articles, details_articles,about
urlpatterns = [
    path('',home, name='index'),
    path('about/',about, name='about'),
    path('details/<int:id>/',details, name='details'),
    path('articles/list/',list_articles, name='list_articles'),
    path('articles/details/<int:id>',details_articles, name='details_articles'),
]
