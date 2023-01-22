from django.urls import path
from . import views

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('createnew/', views.createNew.as_view(), name='createnew'),
    path('loginpage/', views.loginPage.as_view(), name='login'),
]
