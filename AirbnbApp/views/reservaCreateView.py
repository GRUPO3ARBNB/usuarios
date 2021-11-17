from django.conf import settings
from django.http.response import ResponseHeaders
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from AirbnbApp.models.reserva import Reserva
from AirbnbApp.models.user import User
