from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LoginView
from . import views
# from django.conf import settings
# from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('search/', views.search, name='search'),


    path("", views.index, name="index"),
    path("", views.search, name="search"),
    path("", views.login, name="login"),
    path("", views.signup, name="signup"),


    ]

