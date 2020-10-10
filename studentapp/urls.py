from django.urls import path, include
from studentapp.views import *
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

router=routers.DefaultRouter()
router.register('student', Studentview, basename='student')
schema_view=get_swagger_view(title="student api documentation")
urlpatterns = [
    path('', include(router.urls)),
    path('api_documentation', schema_view),
]
