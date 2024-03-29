# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-10-16 21:52
from __future__ import unicode_literals

import cms.apps.media.models
import cms.models.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pages', '0006_auto_20151002_1655'),
        ('media', '0010_auto_20190523_1638'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_online', models.BooleanField(default=True, help_text="Uncheck this box to remove the page from the public website. Logged-in admin users will still be able to view this page by clicking the 'view on site' button.", verbose_name='online')),
                ('browser_title', models.CharField(blank=True, help_text="The heading to use in the user's web browser. Leave blank to use the page title. Search engines pay particular attention to this attribute.", max_length=1000)),
                ('meta_description', models.TextField(blank=True, help_text='A brief description of the contents of this page.', verbose_name='description')),
                ('sitemap_priority', models.FloatField(blank=True, choices=[(1.0, 'Very high'), (0.8, 'High'), (0.5, 'Medium'), (0.3, 'Low'), (0.0, 'Very low')], default=None, help_text='The relative importance of this content on your site. Search engines use this as a hint when ranking the pages within your site.', null=True, verbose_name='priority')),
                ('sitemap_changefreq', models.IntegerField(blank=True, choices=[(1, 'Always'), (2, 'Hourly'), (3, 'Daily'), (4, 'Weekly'), (5, 'Monthly'), (6, 'Yearly'), (7, 'Never')], default=None, help_text='How frequently you expect this content to be updated. Search engines use this as a hint when scanning your site for updates.', null=True, verbose_name='change frequency')),
                ('robots_index', models.BooleanField(default=True, help_text='Uncheck to prevent search engines from indexing this page. Do this only if the page contains information which you do not wish to show up in search results.', verbose_name='allow indexing')),
                ('robots_follow', models.BooleanField(default=True, help_text='Uncheck to prevent search engines from following any links they find in this page. Do this only if the page contains links to other sites that you do not wish to publicise.', verbose_name='follow links')),
                ('robots_archive', models.BooleanField(default=True, help_text='Uncheck this to prevent search engines from archiving this page. Do this this only if the page is likely to change on a very regular basis. ', verbose_name='allow archiving')),
                ('og_title', models.CharField(blank=True, help_text='Title that will appear on Facebook posts. This is limited to 100 characters, but Facebook will truncate the title to 88 characters.', max_length=100, verbose_name='title')),
                ('og_description', models.TextField(blank=True, help_text='Description that will appear on Facebook posts. It is limited to 300 characters, but it is recommended that you do not use anything over 200.', max_length=300, verbose_name='description')),
                ('twitter_card', models.IntegerField(blank=True, choices=[(0, 'Summary'), (1, 'Photo'), (2, 'Video'), (3, 'Product'), (4, 'App'), (5, 'Gallery'), (6, 'Large Summary')], default=None, help_text='The type of content on the page. Most of the time "Summary" will suffice. Before you can benefit from any of these fields make sure to go to https://dev.twitter.com/docs/cards/validation/validator and get approved.', null=True, verbose_name='card')),
                ('twitter_title', models.CharField(blank=True, help_text='The title that appears on the Twitter card, it is limited to 70 characters.', max_length=70, verbose_name='title')),
                ('twitter_description', models.TextField(blank=True, help_text="Description that will appear on Twitter cards. It is limited to 200 characters. This does'nt effect SEO, so focus on copy that complements the tweet and title rather than on keywords.", max_length=200, verbose_name='description')),
                ('slug', models.SlugField(help_text='A user friendly URL')),
                ('title', models.CharField(max_length=1000)),
                ('short_title', models.CharField(blank=True, help_text='A shorter version of the title that will be used in site navigation. Leave blank to use the full-length title.', max_length=200)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('summary', models.TextField(blank=True)),
                ('content', cms.models.fields.HtmlField()),
                ('image', cms.apps.media.models.ImageRefField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='media.File')),
                ('og_image', cms.apps.media.models.ImageRefField(blank=True, help_text='The recommended image size is 1200x627 (1.91:1 ratio); this gives you a big stand out thumbnail. Using an image smaller than 400x209 will give you a small thumbnail and will splits posts into 2 columns. If you have text on the image make sure it is centered.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='media.File', verbose_name='image')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='NewsFeed',
            fields=[
                ('page', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='+', serialize=False, to='pages.Page')),
                ('per_page', models.IntegerField(default=12, verbose_name='Articles per page')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='article',
            name='page',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='news.NewsFeed', verbose_name='News feed'),
        ),
        migrations.AddField(
            model_name='article',
            name='twitter_image',
            field=cms.apps.media.models.ImageRefField(blank=True, help_text='The minimum size it needs to be is 280x150. If you want to use a larger imagemake sure the card type is set to "Large Summary".', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='media.File', verbose_name='image'),
        ),
        migrations.AlterUniqueTogether(
            name='article',
            unique_together=set([('page', 'slug')]),
        ),
    ]
