from django.conf import settings
from django.db import models

from django.core.validators import RegexValidator
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

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

@register_snippet
class MapStyle(models.Model):
    name = models.CharField(max_length=255)

    panels = [
        FieldPanel('name'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'map styles'


class MapsIndexPage(Page):
    """
    A Page model that creates an index page (a listview)
    """
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

    # Only LocationPage objects can be added underneath this index page
    subpage_types = ['MapPage']

    # Allows children of this indexpage to be accessible via the indexpage
    # object on templates. We use this on the homepage to show featured
    # sections of the site and their child pages
    def children(self):
        return self.get_children().specific().live()

    # Overrides the context to list all child
    # items, that are live, by the date that they were published
    # http://docs.wagtail.io/en/latest/getting_started/tutorial.html#overriding-context
    def get_context(self, request):
        context = super(MapsIndexPage, self).get_context(request)
        context['maps'] = MapPage.objects.descendant_of(
            self).live().order_by(
            'title')
        return context

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
        ImageChooserPanel('image'),
    ]

class MapPage(Page):
    """
    Detail for a map.
    """
    intro = models.TextField(
        help_text='Text to describe the page',
        blank=True)
    date = models.DateField("Map date", blank=True, null=True)
    image = models.ForeignKey(
        'base.CustomImage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Map thumbnail'
    )
    body = StreamField(
        BaseStreamBlock(), verbose_name="Page body", blank=True
    )
    layer = models.TextField(
        help_text='GeoServer WMS layer name',
        blank=True)
    map_style = models.ForeignKey('maps.MapStyle', blank=True, null=True, on_delete=models.SET_NULL)
    long_lat = models.CharField(
        max_length=36,
        null=True,
        blank=True,
        help_text="Comma separated long/lat. (Ex. Torino is 7.676111, 45.079167)",
        validators=[
            RegexValidator(
                regex=r'^(\-?\d+(\.\d+)?),\s*(\-?\d+(\.\d+)?)$',
                message='Lat Long must be a comma-separated numeric long and lat',
                code='invalid_long_lat'
            ),
        ]
    )
    zoom = models.TextField(
        max_length=2,
        help_text='Zoom level. Must be between 0 and 18',
        blank=True)

    # Search index configuration
    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    # Fields to show to the editor in the admin view
    content_panels = [
        FieldPanel('title', classname="full"),
        FieldPanel('intro', classname="full"),
        FieldPanel('date'),
        ImageChooserPanel('image'),
        StreamFieldPanel('body'),
        FieldPanel('layer'),
        SnippetChooserPanel('map_style'),
        FieldPanel('long_lat'),
        FieldPanel('zoom'),
    ]

    def __str__(self):
        return self.title


    # Makes additional context available to the template so that we can access
    # the latitude, longitude and map API key to render the map
    def get_context(self, request):
        context = super(MapPage, self).get_context(request)
        context['lat'] = self.long_lat.split(",")[0]
        context['long'] = self.long_lat.split(",")[1]
        context['mapbox_api_token'] = settings.MAPBOX_API_TOKEN
        return context

    # Can only be placed under a MapsIndexPage object
    parent_page_types = ['MapsIndexPage']
