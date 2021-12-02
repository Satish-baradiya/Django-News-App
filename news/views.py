import re
from django.shortcuts import render
from django.http import HttpResponse
import requests
import datetime

# Create your views here.


def index(request):
    url = "https://indian-news-live.p.rapidapi.com/news/"

    headers = {
        'x-rapidapi-host': "indian-news-live.p.rapidapi.com",
        'x-rapidapi-key': ""
        }

    response = requests.request("GET", url, headers=headers)


    titles = [i['title'] for i in response.json()]
    urls = [j['url'] for j in response.json()]
    images = [k['img'] for k in response.json()]
    final_news = zip(titles,urls,images)
    date = datetime.date.today()

    if not response.json():
        return HttpResponse("<h1>No News Found</h1>")
    else:
        return render(request,"news/index.html",{
            "final_news":final_news,
            "date":date     
        })
   