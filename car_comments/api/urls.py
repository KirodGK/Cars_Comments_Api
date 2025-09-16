from django.urls import path, include, re_path
from rest_framework.routers import SimpleRouter
from .views import (
    CountryViewSet,
    ManufacturerViewSet,
    CarViewSet,
    CommentViewSet,
    ExportView
)

router = SimpleRouter()
router.register(r'countries', CountryViewSet, basename="countries")
router.register(r'manufacturers', ManufacturerViewSet,
                basename="manufacturers")
router.register(r'cars', CarViewSet, basename="cars")
router.register(r'comments', CommentViewSet, basename="comments")

urlpatterns = [
    path('export/', ExportView.as_view(), name='export'),
    path('', include(router.urls)),
    path('', include('rest_framework.urls', namespace='rest_framework')),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
