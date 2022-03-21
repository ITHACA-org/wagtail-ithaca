from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.core.blocks import (
    CharBlock, ChoiceBlock, RichTextBlock, StreamBlock, StructBlock, TextBlock, RawHTMLBlock
)


class ImageBlock(StructBlock):
    image = ImageChooserBlock(required=True)
    caption = CharBlock(required=False)
    attribution = CharBlock(required=False)

    class Meta:
        icon = 'image'
        template = "blocks/image_block.html"


class HeadingBlock(StructBlock):
    heading_text = CharBlock(classname="title", required=True)
    size = ChoiceBlock(choices=[
        ('', 'Select a header size'),
        ('h2', 'H2'),
        ('h3', 'H3'),
        ('h4', 'H4')
    ], blank=True, required=False)

    class Meta:
        icon = "title"
        template = "blocks/heading_block.html"


class BlockQuote(StructBlock):
    """
    Custom `StructBlock` that allows the user to attribute a quote to the author
    """
    text = TextBlock()
    attribute_name = CharBlock(
        blank=True, required=False, label='e.g. Mary Berry')

    class Meta:
        icon = "fa-quote-left"
        template = "blocks/blockquote.html"

class SnippetBlock(StructBlock):
    """
    Custom `StructBlock` that allows the user to attribute a quote to the author
    """
    text = RichTextBlock()
    attribute_name = CharBlock(
        blank=True, required=False, label='e.g. Mary Berry')

    class Meta:
        icon = "fa-text-height"
        template = "blocks/blockquote.html"

class CodeBlock(StructBlock):
    """
    Custom `StructBlock` that allows the user to insert code
    """
    text = TextBlock()

    class Meta:
        icon = "fa-code"
        template = "blocks/code_block.html"

class Map1Block(StructBlock):
    """
    Custom block that allows the user to insert pre-defined maps.
    """
    caption = CharBlock(required=False)
    attribution = CharBlock(required=False)
    class Meta:
        icon = 'fa-globe-asia'
        template = "blocks/tonga1_block.html"

class Map2Block(StructBlock):
    """
    Custom block that allows the user to insert pre-defined maps.
    """
    caption = CharBlock(required=False)
    attribution = CharBlock(required=False)
    class Meta:
        icon = 'fa-globe-asia'
        template = "blocks/tonga2_block.html"

class Map3Block(StructBlock):
    """
    Custom block that allows the user to insert pre-defined maps.
    """
    caption = CharBlock(required=False)
    attribution = CharBlock(required=False)
    class Meta:
        icon = 'fa-globe-asia'
        template = "blocks/tonga3_block.html"

class MapBlock (StructBlock):
    """
    Custom block that allows the user to insert pre-defined maps.
    """
    map = RawHTMLBlock (required=True)
    caption = CharBlock(required=False)
    attribution = CharBlock(required=False)
    class Meta:
        icon = 'fa-map'
        template = "blocks/map_block.html"

class MapJS (RawHTMLBlock):
    """
    Custom block that allows the user to insert pre-defined maps.
    """
    class Meta:
        icon = 'fa-js'
        template = "blocks/js_block.html"

class MapCSS (RawHTMLBlock):
    """
    Custom block that allows the user to insert pre-defined maps.
    """
    class Meta:
        icon = 'fa-css3-alt'
        template = "blocks/js_block.html"

class ComparisonBlock (RawHTMLBlock):
    """
    Custom block that allows the user to insert pre-defined maps.
    """
    caption = CharBlock(required=False)
    attribution = CharBlock(required=False)
    class Meta:
        icon = 'fa-code-compare'
        template = "blocks/comparison_block.html"

class BaseStreamBlock(StreamBlock):
    """
    Define the custom blocks that `StreamField` will utilize
    """
    heading_block = HeadingBlock()
    paragraph_block = RichTextBlock(
        icon="paragraph",
        template="blocks/paragraph_block.html")
    image_block = ImageBlock()
    block_quote = BlockQuote()
    code_block = CodeBlock(
        help_text='Insert code',
        icon="fa-code",
        template="blocks/code_block.html")
    embed_block = EmbedBlock(
        help_text='Insert an embed URL e.g https://www.youtube.com/watch?v=OrOE2y0Fj2w',
        icon="fa-s15",
        template="blocks/embed_block.html")
    map1_block = Map1Block(
        help_text='Insert caption for map',
        icon="fa-globe-asia",
        template="blocks/tonga1_block.html")
    map2_block = Map2Block(
        help_text='Insert caption for map',
        icon="fa-globe-asia",
        template="blocks/tonga2_block.html")
    map3_block = Map3Block(
        help_text='Insert caption for map',
        icon="fa-globe-asia",
        template="blocks/tonga3_block.html")
    map_block = MapBlock (
        help_text='<div id="map" class="col-md-12 mapboxgl-map">',
        icon="fa-map",
        template="blocks/map_block.html")
    js_block = MapJS (
        help_text='Included in <script> tags',
        icon="fa-js",
        template="blocks/js_block.html")
    css_block = MapCSS (
        help_text='Included in <style> tags',
        icon="fa-css3-alt",
        template="blocks/css_block.html")
    comparison_block = ComparisonBlock (
        help_text='Included in <script> tags',
        icon="fa-code-compare",
        template="blocks/comparison_block.html")
    snippet_block = SnippetBlock (
        help_text = "Insert your snippet text",
        icon = "fa-text-height",
        template = "blocks/central_snippet.html"
    )
