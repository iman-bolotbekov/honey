from django.http import HttpResponseRedirect
from rest_framework import viewsets

from .models import Client, ConfirmAccount
from .serializers import ClientSerializer, ConfirmSerializer
from django.urls import reverse_lazy


class ClientViewSet(viewsets.mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ConfirmViewSet(viewsets.mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = ConfirmAccount.objects.all()
    serializer_class = ConfirmSerializer
