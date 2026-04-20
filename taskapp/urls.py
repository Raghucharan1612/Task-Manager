from django.urls import path
from . import views   # ✅ correct

urlpatterns = [
    path('', views.home),
    path('add/', views.add_task),
    path('delete/<int:id>/', views.delete_task),
    path('complete/<int:id>/', views.complete_task),
]