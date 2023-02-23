from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404

from .models import Tare, Honey, Basket, Feedback
from .serializers import TareSerializer, HoneySerializer, BasketSerializer, FeedbackSerializer


class HoneyListCreateAPIView(generics.ListCreateAPIView):
    queryset = Honey.objects.all()
    serializer_class = HoneySerializer
    # permission_classes = [permissions.IsAdminUser, ]

    def perform_create(self, serializer):
        # if AttributeError:
        #     return Response('У вас нет доступа!', status=status.HTTP_403_FORBIDDEN)
        if self.request.user.client:
            serializer.save(client=self.request.user.client)


class HoneyRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Honey.objects.all()
    serializer_class = HoneySerializer
    # permission_classes = [permissions.IsAdminUser, ]


class BasketListCreateAPIView(generics.ListCreateAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get_queryset(self):
        return super().get_queryset().filter(honey_id=self.kwargs.get('honey_id'))

    def perform_create(self, serializer):
        basket = get_object_or_404(Honey, pk=self.kwargs.get('honey_id'))
        basket.quantity += 1
        serializer.save(client=self.request.user.client, honey_id=self.kwargs.get('honey_id'))


class BasketRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]


class FeedbackListCreateAPIView(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def perform_create(self, serializer):
        serializer.save(client=self.request.user.client)


class FeedbackRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]
