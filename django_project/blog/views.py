from django.shortcuts import render


posts = [
    {'author': 'MartyMart',
     'title': 'BloggyBlog 1',
     'content': 'First Post',
     'date_posted': '19 juni 2023'
     },
     {'author': 'ForsbyFors',
     'title': 'BloggyBlog 2',
     'content': 'Second Post',
     'date_posted': '19 juni 2023'
     }
]

# Create your views here.
def home(request):

    # Keys in here is available in the template throught the context
    context = {
        'posts':posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title':'About'})