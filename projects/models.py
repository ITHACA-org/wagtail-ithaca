from django import forms

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db import models

from modelcluster.fields import ParentalKey, ParentalManyToManyField

from wagtail.admin.edit_handlers import (
    FieldPanel, InlinePanel, MultiFieldPanel, StreamFieldPanel
    )
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Orderable, Page
from wagtail.search import index
from wagtail.snippets.models import register_snippet
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from base.blocks import BaseStreamBlock

class ProjectPage(Page):
    intro = models.TextField(
        help_text='Text to describe the page',
        blank=True)
    image = models.ForeignKey(
        'base.CustomImage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Landscape mode only; horizontal width between 1000px and 3000px.'
    )
    body = StreamField(
        BaseStreamBlock(), verbose_name="Page body", blank=True
    )

    is_featured = models.BooleanField(
        default=False,
        help_text='Featured projects will appear on the home page'
    )

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
        FieldPanel('is_featured'),
        ImageChooserPanel('image'),
        StreamFieldPanel('body')
    ]

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    parent_page_types = ['ProjectsIndexPage']


class ProjectsIndexPage(Page):
    intro = models.TextField(
        help_text='Text to describe the page',
        blank=True)
    image = models.ForeignKey(
        'base.CustomImage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Landscape mode only; horizontal width between 1000px and '
        '3000px.'
    )
    body = StreamField(
        BaseStreamBlock(), verbose_name="Page body", blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
        ImageChooserPanel('image'),
        StreamFieldPanel('body'),
    ]

    # Can only have ProjectPage children
    subpage_types = ['ProjectPage']

    # Returns a queryset of ProjectPage objects that are live, that are direct
    # descendants of this index page with most recent first
    def get_projects(self):
        return ProjectPage.objects.live().descendant_of(
            self).order_by('-first_published_at')

    # Allows child objects (e.g. ProjectPage objects) to be accessible via the
    # template. We use this on the HomePage to display child items of featured
    # content
    def children(self):
        return self.get_children().specific().live().order_by('-first_published_at')

    # Pagination for the index page. We use the `django.core.paginator` as any
    # standard Django app would, but the difference here being we have it as a
    # method on the model rather than within a view function
    def paginate(self, request, *args):
        page = request.GET.get('page')
        paginator = Paginator(self.get_projects(), 12)
        try:
            pages = paginator.page(page)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)
        return pages

    # Returns the above to the get_context method that is used to populate the
    # template
    def get_context(self, request):
        context = super(ProjectsIndexPage, self).get_context(request)

        # ProjectPage objects (get_projects) are passed through pagination
        projects = self.paginate(request, self.get_projects())

        context['projects'] = projects

        return context
