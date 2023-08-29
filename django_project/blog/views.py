from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    # Keys in here is available in the template throught the context
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})