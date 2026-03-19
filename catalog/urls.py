from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('',          views.creature_list,   name='list'),
    path('nueva/',    views.creature_create, name='create'),
    path('<int:pk>/', views.creature_detail, name='detail'),
]
