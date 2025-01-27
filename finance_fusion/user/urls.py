from django.urls import path
from .views.register_user import CustomUserListCreate, SuperuserListCreate
from .views.update_user import CustomUserDetails
from .views.login_user import Loginview

urlpatterns = [
    path('', CustomUserListCreate.as_view(), name='register_user'),
    path('login/', Loginview.as_view(), name='login_user'),
    path('superuser/', SuperuserListCreate.as_view(), name='register_superuser'),
    path('<int:id>/', CustomUserDetails.as_view(), name='update_user'),
]

