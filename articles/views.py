from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .form import ArticleForm
from .models import Article
# Create your views here.
# Article=''
def home(request):
    # articles = Article.objects.all()
    object_list = Article.objects.filter(archive=False).order_by('-last_update')
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
    

def about(request):
    return render(request, 'pages/about.html')


def details(request, id):
    
    article = get_object_or_404(Article, id=id)
   
    
    return render(request, 'pages/details.html',{'article':article})

@login_required(login_url='/login/')
def list_articles(request):
    user = request.user
    object_list = Article.objects.filter(author=user, archive = False).order_by('-last_update')
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

@login_required(login_url='/login/')
def new_articles(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            author = request.user
            title =  request.POST['title']
            summary = request.POST['summary']
            content =  request.POST['content']
            article = Article.objects.create(
                author = author,
                title = title,
                summary = summary,
                content = content
            )
            article.save()
            
            return redirect('/articles/list/')
    
    else:
       form = ArticleForm() 
    
    return render (request, 'articles/new_articles.html', {'form':form} )


@login_required(login_url='/login/')
def edit_articles(request,id):
    article = get_object_or_404(Article, id=id)
    
    form =ArticleForm(instance=article)
    if request.method == 'POST':
        title =  request.POST['title']
        summary = request.POST['summary']
        content =  request.POST['content']
        article_to_update = Article.objects.filter(pk=article.id)
        article_to_update.update(
             title = title,
            summary = summary,
            content = content,
            
        )
        
        return redirect('/articles/list/')

    return render (request, 'articles/edit_articles.html',{'article':article,'form':form})



@login_required(login_url='/login/')
def delete_article(request, id):
    article =get_object_or_404(Article, id=id)
    if request.method == 'POST':
        article_to_delete = Article.objects.filter(pk=article.id)
        article_to_delete.update(
            archive =True
        )
        # article.delete()
        return redirect('/articles/list/')
    return render(request, 'articles/delete_articles.html', {'article': article})

 
