from .sitemaps import ProjectSitemap
from django.urls import path, re_path
from .sitemaps import ProjectSitemap
from . import views


sitemaps = {
    'project': ProjectSitemap,
}

urlpatterns = [
    path('', views.index_en, name='index_en'),
    path('ru/', views.index_ru, name='index_ru'),
    path('zh/', views.index_zh, name='index_zh'),
    re_path(r'^(?P<lang>[^/]+)/(?P<slug>[\w\-а-яА-Я]+)/$', views.project_detail, name='project_detail'),
    re_path(r'^(?P<slug>[\w\-а-яА-Я]+)/$', views.project_detail, {'lang': 'en'}, name='project_detail_no_lang'),
]







