from django.urls import path
from . import views

urlpatterns = [
    path('', views.page1, name='aboutus_page1'),
    path('2/', views.page2, name='aboutus_page2'),
]
