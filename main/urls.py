from django.urls import path
from . import views 

app_name = 'main'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'), 
    path('profile/<int:pk>', views.ProfileDetailView.as_view(), name='profile'),
    path('profile_update/<int:pk>', views.ProfileUpdateView.as_view(), name='profile_update'),
    path('incomplete_profile', views.incomplete_profile, name="incomplete_profile")
]
