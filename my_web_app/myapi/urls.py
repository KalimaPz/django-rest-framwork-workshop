from django.urls import path , include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('person',views.PersonViewset)
router.register('employee',views.EmployeeViewset)
urlpatterns = [
    path('api/',include(router.urls)),
    # path('api-auth/',include('rest_framework.urls',namespace='rest_framework'))
]
