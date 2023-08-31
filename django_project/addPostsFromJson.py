import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")
import django
django.setup()
import json
from django.contrib.auth.models import User
from blog.models import Post

with open('posts.json') as f:
    posts = json.load(f)
    

for post in posts:
    user_id = post['user_id']
    author = User.objects.get(id=user_id)
    new_post = Post(title=post['title'], content=post['content'], author=author)
    new_post.save()       