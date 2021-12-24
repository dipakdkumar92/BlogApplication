from django.shortcuts import get_object_or_404, render
from blog.forms import ArticleForm
from django.conf import settings
from blog.models import Article, Tag
from django.shortcuts import redirect
from django.utils import translation


def index(request):
    user_language = settings.LANGUAGE_CODE
    translation.activate(user_language)
    tags = request.GET.keys()
    articles = None
    if tags:
        articles = Article.objects.filter(tags__name__in=list(tags))
    else:
        articles = Article.objects.all()
    context = {
        'articles': articles,
        'tags': Tag.objects.all(),
        'selected_tags': list(tags),
    }
    return render(request, 'index.html', context=context)


def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, request.FILES)
        article = article_form.save()
        tags = request.POST.get('tags')
        if tags:
            for tag_id in request.POST.get('tags'):
                tag = Tag.objects.get(id=tag_id)
                article.tags.add(tag)
        return redirect("blog:index")
    return render(request, 'create_article.html', {"form": ArticleForm()})


def detail(request, id):
    article = get_object_or_404(Article, id=id)
    context = {
        'article': article,
    }
    return render(request, 'detail.html', context=context)