from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('detail/<int:id>', views.detail, name="detail"),

]
