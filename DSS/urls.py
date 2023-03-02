from django.urls import path

from DSS.views import ClothesCreateView, ClothesView, PersonView

urlpatterns = [
    path('clothes/create', ClothesCreateView.as_view()),
    path('clothes/<pk>', ClothesView.as_view()),
    path('person/<pk>', PersonView.as_view()),
]