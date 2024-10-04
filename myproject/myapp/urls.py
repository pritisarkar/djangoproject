from django.urls import path
from myapp import views
urlpatterns = [
    path('createmp/', views.employee,name="createmp"),
    path('fetch/',views.fetch_employee,name="fetch"),
    path('update/', views.update_employee,name="update")
]