from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Car, Comment, Country, Manufacturer
from .permissions import PostGetForAllOthersForUserOrAdmin
from .serializers import (
    CarSerializer,
    CommentSerializer,
    CountrySerializer,
    ManufacturerSerializer
)

from .utils import export_csv, export_xlsx


class CountryViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['get'])
    def manufacturers(self, request, pk=None):
        country = self.get_object()
        manufacturers = Manufacturer.objects.filter(country=country)
        serializer = ManufacturerSerializer(manufacturers, many=True)
        return Response(serializer.data)


class ManufacturerViewSet(ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['get'])
    def country(self, request, pk=None):
        manufacturer = self.get_object()
        country = manufacturer.country
        serializer = CountrySerializer(country)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def cars(self, request, pk=None):
        manufacturer = self.get_object()
        cars = Car.objects.filter(manufacturer=manufacturer)
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)


class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['get'])
    def manufacturer(self, request, pk=None):
        car = self.get_object()
        manufacturer = car.manufacturer
        serializer = ManufacturerSerializer(manufacturer)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def comments(self, request, pk=None):
        car = self.get_object()
        comments = Comment.objects.filter(car=car)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [PostGetForAllOthersForUserOrAdmin]


class ExportView(APIView):
    def get(self, request):
        print("query_params:", dict(request.query_params))
        print("GET:", dict(request.GET))
        format_type = request.query_params.get('export_format', 'xlsx')

        if format_type == 'csv':
            return export_csv(self)
        elif format_type == 'xlsx':
            return export_xlsx(self)
        else:
            return Response(
                {"error": "Unsupported format. Use 'csv' or 'xlsx'."},
                status=400
            )

    def get_export_data(self):
        return {
            'countries': Country.objects.all(),
            'manufacturers': Manufacturer.objects.select_related(
                'country').all(),
            'cars': Car.objects.select_related(
                'manufacturer__country').all(),
            'comments': Comment.objects.select_related(
                'car__manufacturer').all(),
        }
