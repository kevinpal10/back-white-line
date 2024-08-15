from django.urls import path, include
from rest_framework import routers
from api import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

router = routers.DefaultRouter()
router.register(r'persona', views.PersonaViewSet)


urlpatterns = [
    path('',include(router.urls))
]

urlpatterns += staticfiles_urlpatterns()