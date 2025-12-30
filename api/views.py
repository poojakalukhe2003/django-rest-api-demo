from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Avg
import requests

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


@api_view(['GET'])
def weather_api(request):
    try:
        response = requests.get(
            "https://api.open-meteo.com/v1/forecast"
            "?latitude=19.0760&longitude=72.8777"
            "&current_weather=true",
            timeout=5
        )
        response.raise_for_status()
        return Response(response.json())
    except requests.exceptions.RequestException:
        return Response(
            {"error": "Failed to fetch weather data"},
            status=500
        )


@api_view(['GET'])
def product_report(request):
    total_products = Product.objects.count()
    average_price = Product.objects.aggregate(avg_price=Avg('price'))

    return Response({
        "total_products": total_products,
        "average_price": average_price["avg_price"]
    })