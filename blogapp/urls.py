from django.urls import path
from blogapp import views

urlpatterns = [
    path("", views.blogapp_index, name="blogapp_index"),
    path("post/<int:pk>/", views.blogapp_detail, name="blogapp_detail"),
    path("category/<category>/", views.blogapp_category, name="blogapp_category"),
]
