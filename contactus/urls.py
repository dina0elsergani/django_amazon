from django.urls import path
from . import views

urlpatterns = [
    path('', views.page1, name='contactus_page1'),
    path('2/', views.page2, name='contactus_page2'),
]
