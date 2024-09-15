from django.urls import path
from .views import MangasListView, MangasDetailView


urlpatterns = [
    path('', MangasListView.as_view(), name="mangas-list"),
    path('detail/<int:pk>', MangasDetailView.as_view(), name="mangas-detail")
]
