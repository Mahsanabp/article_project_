from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    return render(request, "home.html", {})
    


def article_list(request):
    return render(request, "article.html", {})
    

def contact(request):
    return render(request, "contact.html", {})
