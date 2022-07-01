from django.urls import path
from .views import AddRetrive
from .views import GetProfile
from .views import ExpenseRetrive

urlpatterns = [
    path('', AddRetrive.as_view(), name='index'),
    path("profile/" , GetProfile.as_view(), name ='getprofile' ),
    path("addexpense/" , ExpenseRetrive.as_view(), name='addexpense')
]