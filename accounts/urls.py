from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    # Authentication
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    # User profile
    path('profile/<int:pk>/', views.UserProfileView.as_view(), name='profile'),
    path('edit-profile/', views.UserEditProfileView.as_view(), name='edit_profile'),
]
