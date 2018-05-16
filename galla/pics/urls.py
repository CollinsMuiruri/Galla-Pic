from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
url(r'^$',views.galla_pics, name='gallapics'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^article/(?P<article_id>\d+)',views.article,name ='article'),
    url(r'^(?P<id>\d+)/$',views.article_detail,name = 'detail'),
    url(r'^today-pics/', views.pics_today, name='picsToday'),
    url(r'^gallapics/', views.galla_pics, name='gallapics'),
    url(r'^image/(\d+)', views.image, name='image'),
    # url(r'^search/$', views.search, name='search'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
