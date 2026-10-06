from django.shortcuts import get_object_or_404, render
from blog.models import Post, Category

POSTS_PER_PAGE = 5


def index(request):
    template = 'blog/index.html'
    post_list = Post.objects.published()[:POSTS_PER_PAGE]
    context = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request, id):
    template = 'blog/detail.html'
    post = get_object_or_404(Post.objects.published(),
                             pk=id,
                             )
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(Category,
                                 slug=category_slug,
                                 is_published=True,
                                 )
    post_list = Post.objects.published().filter(
        category=category
    )
    context = {'category': category,
               'post_list': post_list
               }
    return render(request, template, context)
