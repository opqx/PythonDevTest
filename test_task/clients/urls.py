from django.urls import path
from clients import views


urlpatterns = [
    path('', views.List.as_view(), name="list" ),
    path('view/<int:pk>', views.View.as_view(), name="view" ),
    path('create/', views.Create.as_view(), name="create" ),
    path('update/<int:pk>', views.Update.as_view(), name="update" ),
    path('delete/<int:pk>', views.Delete.as_view(), name="delete" ),
]

