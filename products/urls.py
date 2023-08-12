from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='products_index'),
    path('<int:product_id>/', views.show, name='product_show'),
    path('<int:product_id>/delete/', views.delete, name='product_delete'),
    path('create/', views.create_product, name='product_create'),
    path('edit/<int:product_id>/', views.edit_product, name='product_edit'),
    path('categories/', views.categories, name='categories'),
    path('categories/<int:category_id>/', views.category_detail, name='category_detail'),
    path('categories/create/', views.create_category, name='category_create'),
    path('categories/<int:pk>/edit/', views.CategoryEdit.as_view(), name='category_edit'),
    path('categories/<int:pk>/delete/', views.CategoryDelete.as_view(), name='category_delete'),

]
