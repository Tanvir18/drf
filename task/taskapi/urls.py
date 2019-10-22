from rest_framework import routers
from taskapi.views import UserViewSet
from django.urls import path ,include


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
   
    path(r'', include(router.urls)),
    path(r'rest-auth/', include('rest_auth.urls')),
]

