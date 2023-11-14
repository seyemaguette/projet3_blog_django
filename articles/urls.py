from django.urls import path
from .views import home, details, list_articles, details_articles,about, new_articles, edit_articles, delete_article
urlpatterns = [
    path('',home, name='index'),
    path('about/',about, name='about'),
    path('details/<int:id>/',details, name='details'),
    path('articles/list/',list_articles, name='list_articles'),
    path('articles/details/<int:id>',details_articles, name='details_articles'),
    path('articles/new/',new_articles, name='new_articles'),
    path('articles/edit/<int:id>', edit_articles, name='edit_articles'),
    path('articles/delete/<int:id>', delete_article, name='delete_article'),
]
