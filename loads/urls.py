from django.urls import path 
from . import views

app_name = "loads"
urlpatterns = [
    path('', views.LoadListView.as_view(), name="loads"), 
    path("new_load", views.LoadCreateView.as_view(), name='new_load'), 
    path('my_loads', views.my_loads, name='my_loads'), 
    path('<int:pk>', views.LoadUpdateView.as_view(), name='load_update')
]
