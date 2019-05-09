from django.urls import path

from . import views

app_name = "index"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("preco/", views.PricingView.as_view(), name="pricing"),
    path("administrativo/", views.ManagementView.as_view(), name="management"),
    path("administrativo/metodo-vivencial", views.MetodoVivencialView.as_view(), name="metodo_vivencial")
]
