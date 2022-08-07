from django.urls import include, path
from rest_framework import routers
from apps.books.views import BookViewset

router = routers.DefaultRouter()
router.register(r"books", BookViewset)

urlpatterns = [path("", include(router.urls))]