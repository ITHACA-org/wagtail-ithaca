from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.core.blocks import (
    CharBlock, ChoiceBlock, RichTextBlock, StreamBlock, StructBlock, TextBlock,
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


class CodeBlock(StructBlock):
    """
    Custom `StructBlock` that allows the user to insert code
    """
    text = TextBlock()

    class Meta:
        icon = "fa-code"
        template = "blocks/code_block.html"


class BaseStreamBlock(StreamBlock):
    """
    Define the custom blocks that `StreamField` will utilize
    """
    heading_block = HeadingBlock()
    paragraph_block = RichTextBlock(
        icon="paragraph",
        template="blocks/paragraph_block.html"
    )
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
