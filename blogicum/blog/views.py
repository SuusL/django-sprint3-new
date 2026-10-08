from django.shortcuts import get_object_or_404, render

from blog.models import Category
from blog.utils import get_published_posts

POSTS_PER_PAGE = 5


def index(request):
    """Отображает главную страницу блога со списком последних постов."""
    template = 'blog/index.html'
    post_list = get_published_posts()[:POSTS_PER_PAGE]
    context = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request, post_id):
    """Отображает страницу опубликованного поста."""
    template = 'blog/detail.html'
    post = get_object_or_404(get_published_posts(),
                             pk=post_id,
                             )
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    """Отображает страницу категории с её опубликованными постами."""
    template = 'blog/category.html'
    category = get_object_or_404(Category,
                                 slug=category_slug,
                                 is_published=True,
                                 )
    post_list = get_published_posts().filter(
        category=category
    )
    context = {'category': category,
               'post_list': post_list
               }
    return render(request, template, context)
