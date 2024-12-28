from django.urls import path 
from . import views

app_name = "loads"
urlpatterns = [
    path('', views.LoadListView.as_view(), name="loads"), 
    path('load/<int:pk>', views.LoadDetailView.as_view(), name='load'),
    path('add_load_location', views.add_load_location, name='add_load_location'), 
    path("location_detail/<int:pk>", views.LocationDetailView.as_view(), name="location_detail"), 
    path("new_load", views.LoadCreateView.as_view(), name='new_load'), 
    path('my_loads', views.my_loads, name='my_loads'), 
    path('<int:owner_id>/shipper_loads', views.shipper_loads, name='shipper_loads'), 
    path('<str:user>/bookings', views.my_bookings, name='bookings'), 
    path('<int:pk>', views.LoadUpdateView.as_view(), name='load_update'), 
    path('book_load/<int:pk>', views.book_load,  name='book_load'), 
    path('cancel_booking/<int:pk>', views.cancel_booking, name="cancel_booking"), 
    path('mark_delivered/<int:pk>', views.mark_delivered, name="mark_delivered"), 

]
