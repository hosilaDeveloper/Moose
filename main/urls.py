from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('blog/', blog_page, name='blog'),
    path('blog/<int:pk>/', blog_detail_page, name='detail'),
    path('about/', about_page, name='about'),
]