from django.urls import path

from ads.view.ad import AdView, AdDetailView

urlpatterns = [
    path("", AdView.as_view()),
    path("<int:pk>", AdDetailView.as_view()),
]