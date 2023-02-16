from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CartItem, Product
from .serializers import CartSerializer
from rest_framework import status


# Create your views here.

@api_view(['POST'])
def add_to_cart(request,product_id):
    product = Product.objects.all(Product, pk=product_id)
    serializer = CartSerializer(product, many=True)
    cart = CartItem.objects.all(user=request.user, is_active=True)
    cart.add_to_cart(product_id)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def cart(request):
    """
    List all products, or create a new product.
    """
    if request.method == 'GET': # list products
        cart = CartItem.objects.all()
        serializer = CartSerializer(cart, many=True)
        return Response(serializer.data)

    elif request.method == 'POST': # create new product
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    
