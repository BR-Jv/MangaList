from django.urls import path
from .views import MangasListView, MangasDetailView, MangasUpdateView, MangasDeleteView, MangasCreateView


urlpatterns = [
    path('', MangasListView.as_view(), name="mangas-list"),
    path('detail/<int:pk>', MangasDetailView.as_view(), name="mangas-detail"),
    path('update/<int:pk>', MangasUpdateView.as_view(), name="mangas-update"),
    path('delete/<int:pk>', MangasDeleteView.as_view(), name="mangas-delete"),
    path('create/', MangasCreateView.as_view(), name="mangas-create")
]
