from django.shortcuts import render
from .models import Article

# Create your views here.



def article(request):

    context = {
        'articles': Article.objects.all()

    }

    search = request.POST.get('q')
    if search :
        context['articles'] = Article.objects.filter(name__icontains=search)

    return render(request, 'article.html', context)   