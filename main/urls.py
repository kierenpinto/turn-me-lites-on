from django.urls import path
from . import views
app_name = 'main'
urlpatterns = [
    path('<int:pk>/delete',views.DeleteLight.as_view(),name='delLight'),
    path('<int:pk>/',views.LightView, name='LightView'),
    path('create',views.CreateLight.as_view(), name='CreateLight'),
    path('',views.IndexView.as_view(),name='IndexView'),
]
