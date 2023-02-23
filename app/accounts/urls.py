from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from . import views as acc_views

acc_router = routers.DefaultRouter()
acc_router.register('register', acc_views.ClientViewSet)
acc_router.register('otp', acc_views.ConfirmViewSet, basename='otp')

urlpatterns = [
    path('api/auth/', include('rest_framework.urls')),
    path('api/auth/token/', obtain_auth_token),
    path('api/accounts/', include(acc_router.urls)),
]