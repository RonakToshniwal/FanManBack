from django.urls import path
from .views import AddRetrive
from .views import GetProfile

urlpatterns = [
    path('', AddRetrive.as_view(), name='index'),
    path("profile/" , GetProfile.as_view(), name ='getprofile' )
]