from django.urls import path
from .views import AddRetrive

urlpatterns = [
    path('', AddRetrive.as_view(), name='index'),
]