from django.urls import path
from . import views

# urlpatterns are basically the url for specific pages of your website
# each path will point to a specific view in the views.py which will then render to a html file
# the name argument is used to refer to the specific path you want without typing out the whole path
# always add a / for example in path eg.(success/) becuase some web browsers automatically add one at the
# and if you don't have it and they add it you get an ERROR

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('createnew/', views.createNew.as_view(), name='createnew'),
    path('loginpage/', views.loginPage.as_view(), name='login'),
    path('registerpage/', views.registerPage.as_view(), name='register'),
    path('success/', views.success.as_view(), name='success'),
    path('groupchat/', views.groupChat.as_view(), name='groupchat'),
    path('logout/', views.logoutPage.as_view(), name='logout'),
]
