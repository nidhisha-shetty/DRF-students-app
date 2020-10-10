from rest_framework import serializers
from .models import Student

class Students(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=('first_name', 'last_name', 'email','id','url', 'gender_female')