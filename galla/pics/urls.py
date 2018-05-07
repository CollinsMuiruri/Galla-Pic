from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
url(r'^$',views.pics_today,name='picsToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_pics,name = 'pastPics'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^article/(?P<article_id>\d+)',views.article,name ='article'),
    url(r'^(?P<id>\d+)/$',views.article_detail,name = 'detail'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
