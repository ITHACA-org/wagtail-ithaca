# Generated by Django 2.2.10 on 2020-03-12 11:00

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0009_auto_20200306_0945'),
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectsIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('intro', models.TextField(blank=True, help_text='Text to describe the page')),
                ('body', wagtail.core.fields.StreamField([('heading_block', wagtail.core.blocks.StructBlock([('heading_text', wagtail.core.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')], required=False))])), ('paragraph_block', wagtail.core.blocks.RichTextBlock(icon='paragraph', template='blocks/paragraph_block.html')), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False))])), ('block_quote', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.TextBlock()), ('attribute_name', wagtail.core.blocks.CharBlock(blank=True, label='e.g. Mary Berry', required=False))])), ('code_block', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.TextBlock())], help_text='Insert code', icon='fa-code', template='blocks/code_block.html')), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/watch?v=OrOE2y0Fj2w', icon='fa-s15', template='blocks/embed_block.html'))], blank=True, verbose_name='Page body')),
                ('image', models.ForeignKey(blank=True, help_text='Landscape mode only; horizontal width between 1000px and 3000px.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='base.CustomImage')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ProjectPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('intro', models.TextField(blank=True, help_text='Text to describe the page')),
                ('body', wagtail.core.fields.StreamField([('heading_block', wagtail.core.blocks.StructBlock([('heading_text', wagtail.core.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')], required=False))])), ('paragraph_block', wagtail.core.blocks.RichTextBlock(icon='paragraph', template='blocks/paragraph_block.html')), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False))])), ('block_quote', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.TextBlock()), ('attribute_name', wagtail.core.blocks.CharBlock(blank=True, label='e.g. Mary Berry', required=False))])), ('code_block', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.TextBlock())], help_text='Insert code', icon='fa-code', template='blocks/code_block.html')), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/watch?v=OrOE2y0Fj2w', icon='fa-s15', template='blocks/embed_block.html'))], blank=True, verbose_name='Page body')),
                ('image', models.ForeignKey(blank=True, help_text='Landscape mode only; horizontal width between 1000px and 3000px.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='base.CustomImage')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
