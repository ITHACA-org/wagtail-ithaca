from django import template
from django.conf import settings

from blog.models import BlogPage
from people.models import PersonPage

register = template.Library()

# Blog feed for home page
@register.inclusion_tag('ithaca/tags/homepage_blog_listing.html', takes_context=True)
def homepage_blog_listing(context, count=6):
    blog_posts = BlogPage.objects.live().in_menu().order_by('-date')[:count]
    return {
        'blog_posts': blog_posts,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }
