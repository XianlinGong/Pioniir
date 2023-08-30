from django.contrib import admin
from .models import Head, Faq


class HeadAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'content',
        'image',
        'published',
    ]


class FaqAdmin(admin.ModelAdmin):
    fields = [
        'question',
        'answer',
        'published',

    ]


# Register your models here.
admin.site.register(Head, HeadAdmin)
admin.site.register(Faq, FaqAdmin)
