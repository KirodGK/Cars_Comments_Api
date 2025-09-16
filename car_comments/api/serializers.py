from rest_framework import serializers
from .models import Country, Manufacturer, Car, Comment


class CountrySerializer(serializers.ModelSerializer):
    manufacturers = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Country
        fields = ('id', 'name', 'manufacturers')


class ManufacturerSerializer(serializers.ModelSerializer):
    cars_count = serializers.SerializerMethodField()

    class Meta:
        model = Manufacturer
        fields = ('id', 'name', 'country', 'cars_count')

    def get_cars_count(self, manufacturer):
        return manufacturer.cars.count()


class CarSerializer(serializers.ModelSerializer):
    comments_count = serializers.SerializerMethodField()
    comments = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Car
        fields = ('id', 'name', 'manufacturer', 'start_year',
                  'end_year', 'comments', 'comments_count')

    def get_comments_count(self, car):
        return car.comments.count()


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'author_email', 'car', 'created_at', 'text')
