from django.urls import path

from DSS.views import ClothesCreateView, ClothesView

urlpatterns = [
    path('create', ClothesCreateView.as_view()),
    path('<pk>', ClothesView.as_view())
]