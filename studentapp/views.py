from django.shortcuts import render
from rest_framework import viewsets
from .serializers import Students
from .models import Student
from rest_framework.authentication import  SessionAuthentication, BasicAuthentication #forauthentication 
from rest_framework.permissions import IsAuthenticated, IsAdminUser #forauthentication 
from django_filters.rest_framework import DjangoFilterBackend #used for filtering data
from rest_framework.filters import OrderingFilter, SearchFilter #OrderingFilter used to sorting; SearchFilter used to search data     

class Studentview(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=Students
    authentication_classes=[SessionAuthentication, BasicAuthentication] #checks for sessionauthentication first, if no sessions are present, then checks for basicauthentication
    permission_classes=[IsAuthenticated, IsAdminUser] #checks for permissions, only if it returns to 'True', further functions will be executed; first it checks if authenticated, if yes then checks for adminuser (used when only admins are allowed to perform the operations)
                                                      #If IsAdminUser is not used then any user loggedin can perform the operations.
    filter_backends=(DjangoFilterBackend, OrderingFilter, SearchFilter)  #used for filtering, seraching, and sorting data
    filter_fields=('gender_female', ) #field names on which filter is to be applied 
    ordering_fields=('last_name','email') #fieldnames on which sorting is to be applied
    ordering=('first_name')  #The records are displayed by first_name(alphabetically) by default, if this is not added then the sequence in which the records were added will be dispalyed
                             #To dispaly it in reverse order (-first_name)
    search_fields=('first_name','last_name') #searches for the query in the 'first_name' field
   
   
   
   #This is alternatively provided by 'django-filter'
    # def get_queryset(self): #used for filtering data
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