from django.utils import timezone

from blog.models import Post


def get_published_posts():
    """Только опубликованные посты с прошедшей датой публикации."""
    return Post.objects.select_related(
        'author', 'category', 'location'
    ).filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True,
    )