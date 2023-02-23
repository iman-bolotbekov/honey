from django.urls import path, include
from . import views

urlpatterns = [
    path('api/shop/honey/', views.HoneyListCreateAPIView.as_view()),
    path('api/shop/honey/<int:pk>/', views.HoneyRetrieveUpdateDestroyAPIView.as_view()),
    path('api/shop/honey/<int:honey_id>/basket/', views.BasketListCreateAPIView.as_view()),
    path('api/shop/honey/<int:honey_id>/basket/<int:pk>/', views.BasketRetrieveUpdateDestroyAPIView.as_view()),
    path('api/shop/feedback/', views.FeedbackListCreateAPIView.as_view()),
    path('api/shop/feedback/<int:pk>/', views.FeedbackRetrieveUpdateDestroyAPIView.as_view()),
]