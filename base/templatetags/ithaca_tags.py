from django import template
from django.conf import settings

from blog.models import BlogPage
from people.models import PersonPage

register = template.Library()


@register.inclusion_tag('tags/homepage_blog_listing.html', takes_context=True)
def homepage_blog_listing(context, count=6):
    posts = BlogPage.objects.live().order_by('-date')[:count]
    return {
        'posts': posts,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }
