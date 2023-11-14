from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Article
# Create your views here.
def home(request):
    # articles = Article.objects.all()
    object_list = Article.objects.all()
    page_num = request.GET.get('page', 1)

    paginator = Paginator(object_list, 10) # 6 employees per page


    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)

    return render(request, 'pages/index.html', {'page_obj': page_obj})
    

def details(request, id):
    
    article = get_object_or_404(Article, id=id)
   
    
    return render(request, 'pages/details.html',{'article':article})

@login_required(login_url='/login/')
def list_articles(request):
    user = request.user
    object_list = Article.objects.filter(author=user, archive = False)
    page_num = request.GET.get('page', 1)

    paginator = Paginator(object_list, 10) # 6 employees per page


    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)

    return render(request, 'articles/list_articles.html', {'page_obj': page_obj})
    
    
@login_required(login_url='/login/')
def details_articles(request, id):
    
    article = get_object_or_404(Article, id=id)
   
    
    return render(request, 'articles/details_articles.html',{'article':article})