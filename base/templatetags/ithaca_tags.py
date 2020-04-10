from django import template
from django.conf import settings
from django.db import models

from blog.models import BlogPage
from people.models import PersonPage
from projects.models import ProjectPage
from wagtail.contrib.settings.models import BaseSetting, register_setting

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
    projects = ProjectPage.objects.exclude(is_featured=False).filter(live=True).order_by('?')[:count]
    return {
        'projects': projects,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }

@register_setting
class SocialMediaSettings(BaseSetting):
    facebook = models.URLField(
        blank=True, help_text='Your Facebook page URL')
    instagram = models.CharField(
        blank=True, max_length=255, help_text='Your Instagram username, without the @')
    linkedin = models.URLField(
        blank=True, help_text='Your LinkedIn page URL')
    twitter = models.URLField(
        blank=True, help_text='Your Twitter page URL')
