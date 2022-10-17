
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets, response
from .serializer import UserSerialzer, CompanySerializer, SingleUserSerializer, SingleCompanySerializer
from .models import Company, MyUser
from .pagination import LimitPagination
from rest_framework import filters
import random
import string
import os
import faker
# Create your views here.

def home_page_createuser(request):
    return render(request, 'index.html')

class UserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.filter(is_admin=False)
    serializer_class = UserSerialzer
    pagination_class = LimitPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'email', 'fname','lname']

    def retrieve(self, request, pk=None):
        queryset = MyUser.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = SingleUserSerializer(user)
        return response.Response(serializer.data)

    
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    pagination_class = LimitPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def retrieve(self, request, pk=None):
        queryset = Company.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = SingleCompanySerializer(user)
        return response.Response(serializer.data)
    
