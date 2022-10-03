from django.conf.urls import url, include
from django.urls import path
from store.views import *
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from store import views

router=DefaultRouter()

urlpatterns = [
    path('', views.ApiOverview, name='home'),
    # path('auth_token/',views.obtain_auth_token,name='auth-token'),
    path('box/create/',create_box,name='create-box'),
    path('box/list/',list_box,name='list-box'),
    path('box/my_list/',my_list_box,name='list-my-box'),
    path('box/update/<str:pk>',update_box,name='update-box'),
    path('box/delete/<str:pk>',delete_box,name='delete-box')

]

