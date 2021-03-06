from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "core/index.html"


class PricingView(TemplateView):
    template_name = "core/pricing.html"


class ManagementView(TemplateView):
    template_name = "core/management.html"


class MetodoVivencialView(TemplateView):
    template_name = "core/metodo_vivencial.html"
