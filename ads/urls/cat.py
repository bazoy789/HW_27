from django.urls import path

from ads.view.cat import CategoryView, CategoryDetailView

urlpatterns = [
    path("", CategoryView.as_view()),
    path("<int:pk>", CategoryDetailView.as_view()),
]