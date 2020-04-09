from django import forms
from django.db import models
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.search import index

from wagtail.snippets.models import register_snippet

from base.blocks import BaseStreamBlock

@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    panels = [
        FieldPanel('name'),
        ImageChooserPanel('icon'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'blog categories'


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
    ]

    # Pagination

    def get_posts(self):
        # Get list of blog pages that are descendants of this page
        get_posts = BlogPage.objects.live().descendant_of(self)

        # Order by most recent date first
        get_posts = get_posts.order_by('-date', 'pk')

        return get_posts

    def paginate(self, request, *args):
        page = request.GET.get('page')
        paginator = Paginator(self.get_posts(), 10)
        try:
            pages = paginator.page(page)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)
        return pages

    # End of pagination

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        #posts = self.get_children().live().order_by('-first_published_at')
        posts = self.paginate(request, self.get_posts())
        context['posts'] = posts
        return context

class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'BlogPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )

class BlogTagIndexPage(Page):

    def get_context(self, request):

        # Filter by tag
        tag = request.GET.get('tag')
        posts = BlogPage.objects.filter(tags__name=tag)

        # Update template context
        context = super().get_context(request)
        context['posts'] = posts
        return context


class BlogPageAuthor(Orderable):
    page = ParentalKey('blog.BlogPage', related_name='authors')
    author = models.ForeignKey(
        'people.Author',
        on_delete=models.CASCADE,
        related_name='+',
    )

    panels = [
        SnippetChooserPanel('author'),
    ]


class BlogPage(Page):
    date = models.DateField("Post date", blank=True, null=True)
    intro = models.CharField(max_length=250, blank=True)
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
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    categories = ParentalManyToManyField('blog.BlogCategory', blank=True)

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    @property
    def has_authors(self):
        return self.authors.exists()

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('tags'),
            FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        ], heading="Blog information"),
        FieldPanel('intro'),
        ImageChooserPanel('image'),
        StreamFieldPanel('body'),
        InlinePanel('authors', label="Author"),
        InlinePanel('related_links', label="Related links"),
        InlinePanel('gallery_images', label="Gallery images"),
    ]

    parent_page_types = ['blog.BlogIndexPage']
    subpage_types = []


class BlogPageRelatedLink(Orderable):
    page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name='related_links')
    name = models.CharField(max_length=255)
    url = models.URLField()

    panels = [
        FieldPanel('name'),
        FieldPanel('url'),
    ]

class BlogPageGalleryImage(Orderable):
    page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]
