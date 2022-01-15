from django.db.models import F

from blog.models import Post


def get_post_by_slug(slug: str) -> Post:
    """returns post instance or 404 on slug"""
    post = Post.objects.filter(slug=slug)
    post.update(post_views=F('post_views') + 1)
    return post[0]
