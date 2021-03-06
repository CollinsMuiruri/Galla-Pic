from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Article
import django_filters
from .filters import ArticleFilter



# Create your views here.
def welcome(request):
    return render(request,'welcome.html')


def galla_pics(request):

    articles = Article.objects.all()
    return render(request,'all-pics/article.html',{'articles' :articles})

# View Function to present pics from past days
def past_days_pics(request, past_date):

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(pics_today)

    return render(request, 'all-pics/past-pics.html', {"date": date})

def pics_today(request):
    date = dt.date.today()
    pics = Article.todays_pics()
    return render(request, 'all-pics/today-pics.html', {"date":date,"pics":pics})


# View Function to present pics from past days
def past_days_pics(request, past_date):
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(pics_today)

    pics = Article.days_pics(date)
    return render(request, 'all-pics/past-pics.html',{"date": date,"pics":pics})


def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-pics/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-pics/search.html',{"message":message})


def article(request,article_id):
    try:
        article = Article.objects.get(id = article_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-pics/article.html", {"article":article})

def article_detail(request,id):
    # return HttpResponse(slug)
    articles = Article.objects.filter(id = id).all()
    return render(request,'articles/article_detail.html',{'articles':article})



def index(request):
    date = dt.date.today()
    articles = Article.objects.filter(id = id).all()

    return render(request,"index.html", {"date":date,"articles": articles})



def search(request):
    user_list = Article.objects.all()
    user_filter = ArticleFilter(request.GET, queryset=user_list)
    return render(request, 'user_list.html', {'filter': user_filter})


def image(request, image_id):

    image = Article.objects.get(id=article_id)

    return render(request, 'image.html', {"image": image})
