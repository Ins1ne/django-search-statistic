# coding: utf-8
from django.shortcuts import render_to_response, get_object_or_404
from example.models import Article
from search_statistic.utils.visits import visit_object


def index(request):
    return render_to_response('example/index.html', {
        'articles': Article.objects.all()
    })


def article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    visit_object(request, article)
    return render_to_response('example/article.html', {
        'article': article
    })
