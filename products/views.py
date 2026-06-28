from rest_framework import viewsets, permissions
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_name = ProductSerializer     
    serializer_class = ProductSerializer

    # Senior Security Pattern: Safe methods (GET) are public.
    # Write methods (POST, PUT, DELETE) require admin credentials.
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]