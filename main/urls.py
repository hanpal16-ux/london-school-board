# urls.py. in the application folder
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home_path'),
    path('contact/', views.contact, name='contact_path'),
    path('about/', views.about, name='about_path'),
    path('student/add/', views.student_form, name='student_form_path'),
    path('student/list/', views.student_list, name='student_list_path'),
    path('product/list/', views.product_listing, name='product_list_path'),
    path('register/', views.register, name='register'),
    path('login/', views.u_login, name='login'),
    path('logout/', views.u_logout, name='logout'),
]