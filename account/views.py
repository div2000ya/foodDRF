from django.shortcuts import render
from rest_framework import response
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from .serializers import RestaurantSerializer,MenuSerializer
from rest_framework.response import Response
from rest_framework.views import status
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import *
# Create your views here.
class SignupAPI(APIView):
    def post(self, request):
        print("request>>", request.data)
        ser = UserSerializer(data = request.data)

        if(ser.is_valid()):
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

class AddRestaurant(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self,request):
        ser = RestaurantSerializer(data=request.data)
        if (ser.is_valid()):
            ser.save()
            return Response(ser.data,status= status.HTTP_201_CREATED)

        return Response(ser.errors,status= status.HTTP_400_BAD_REQUEST)


class AddMenu(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self,request):
        ser = MenuSerializer(data=request.data)
        if (ser.is_valid()):
            ser.save()
            return Response(ser.data,status= status.HTTP_201_CREATED)

        return Response(ser.errors,status= status.HTTP_400_BAD_REQUEST)

class RestaurantDetail(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        res = Restaurant.objects.all()
        ser = RestaurantSerializer(res,many=True)
        return Response(ser.data)

class MenuDetail(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        id = request.GET.get('id')
        if id is not None:
            menu = Fooditem.objects.filter(RestaurantName=id)
            ser = MenuSerializer(menu,many=True)
            return Response(ser.data)

class Placeorder(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self,request):
        ser = Cart(data=request.data)
        if (ser.is_valid()):
            ser.save()
            return Response(ser.data,status= status.HTTP_201_CREATED)

        return Response(ser.errors,status= status.HTTP_400_BAD_REQUEST)