from django import template
from django.conf import settings

from blog.models import BlogPage
from people.models import PersonPage
from projects.models import ProjectPage

register = template.Library()


@register.inclusion_tag('tags/homepage_blog_listing.html', takes_context=True)
def homepage_blog_listing(context, count=3):
    posts = BlogPage.objects.live().order_by('-date')[:count]
    return {
        'posts': posts,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }

@register.inclusion_tag('tags/homepage_projects_listing.html', takes_context=True)
def homepage_projects_listing(context, count=4):
    projects = ProjectPage.objects.filter(live=True).order_by('pk')[:count]
    return {
        'projects': projects,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }
