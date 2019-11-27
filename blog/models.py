from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    def get_context(self, request):
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')
        context['blogpages'] = blogpages
        return context


class BlogPage(Page):
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    date = models.DateField("Post date")

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('date'),
        FieldPanel('body', classname="full"),
    ]
