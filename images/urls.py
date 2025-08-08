from django.urls import path
from .views import upload_image, delete_image

urlpatterns = [
    path('upload/', upload_image),
    path('delete/', delete_image),
]
