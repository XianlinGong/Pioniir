
from django.shortcuts import render
from .models import Head, Faq


def homepage(request):
    matching_heads = Head.objects.all()
    matching_faqs = Faq.objects.all()

    return render(
        request=request,
        template_name='pioniir/homepage.html',
        context={
            "heads": matching_heads,
            "faqs": matching_faqs,
            "type": "homepage"
        }
    )


def price(request):

    return render(
        request=request,
        template_name='pioniir/price.html',
        context={
            "type": "price",
        }
    )
