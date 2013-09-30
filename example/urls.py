from django.conf.urls import patterns, include, url
from example import views

urlpatterns = patterns('',
    url(r'^(\d+)/$', 'example.views.article', name='article'),
    url(r'^$', views.index, name='index'),
)