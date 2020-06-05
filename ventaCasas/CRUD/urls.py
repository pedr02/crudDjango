from django.contrib import admin
from django.urls import path,include
from CRUD import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.viewHouse.as_view(), name='list'),
    path('login/', views.loginUser, name='login'),
    path('register/',views.registerUser, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('create/', views.houseCreate, name='create'),
    path('<int:pk>/details/', views.detailHouse.as_view(), name='view'),
    path('<int:pk>/edit/', views.modifyHouse.as_view(),name='edit'),
    path('<int:pk>/delete/', views.deleteHouse.as_view(),name='delete')
]
