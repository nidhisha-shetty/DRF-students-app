from django.shortcuts import render
from rest_framework import viewsets
from .serializers import Students
from .models import Student
from rest_framework.authentication import  SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework.filters import OrderingFilter, SearchFilter

class Studentview(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=Students
    authentication_classes=[SessionAuthentication, BasicAuthentication]
    permission_classes=[IsAuthenticated, IsAdminUser]
    filter_backends=(DjangoFilterBackend, OrderingFilter, SearchFilter)
    filter_fields=('gender_female', )
    ordering_fields=('last_name','email')
    ordering=('first_name')  #The records are displayed by first_name(alphabetically), if this is not added then the sequence in which the records were added will be dispalyed
                              #To dispaly it in reverse order (-first_name)
    search_fields=('first_name',) #searches for the query in the 'first_name' field
    # def get_queryset(self):
    #     queryset=Student.objects.all()
    #     female=self.request.query_params.get('gender_female', '')
    #     if female:
    #         if female == 'False':
    #             female=False
    #         elif female=='True':
    #             female=True
    #         else:
    #             return queryset
    #         return queryset.filter(gender_female=female)
    #     return queryset