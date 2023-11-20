from django.shortcuts import render
from .models import Postmodel
# Create your views here.


from faker import Faker
import random

fake = Faker()


def generate_fake_blog_data(num_posts):
    for _ in range(num_posts):
        title = fake.sentence()
        content = fake.paragraphs(3)
        pub_date = fake.date_time_this_decade()

        Postmodel.objects.create(title=title, content=content, pub_date=pub_date)


def home_view(request):
    posts = Postmodel.objects.all()
    return render(request, 'home.html', {'posts': posts})


def base_view(request):
    return render(request, 'base.html')


def post_detail_view(request, post_id):
    post = Postmodel.objects.get(pk=post_id)
    return render(request, 'post_detail.html', {'post': post})
