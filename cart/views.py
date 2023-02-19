from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.serializers import ProductSerializer
from product.models import Product
from .models import CartItem
from .serializers import CartSerializer
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404




# Create your views here.

@api_view(['GET', 'POST'])
def cart(request):
    """
    List all cart items, or create a new item.
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
    
class CartDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return CartItem.objects.get(pk=pk)
        except CartItem.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        cart_item = self.get_object(pk)
        serializer = CartSerializer(cart_item)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        cart_item = self.get_object(pk)
        serializer = CartSerializer(cart_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        cart_item = self.get_object(pk)
        cart_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    


@api_view(['POST'])
def add_to_cart(request,product_id):
    if request.method == 'POST': # create new product
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    