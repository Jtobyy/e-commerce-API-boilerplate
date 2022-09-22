from rest_framework import generics

from api.permissions import IsStaffEditorPermission
from .serializers import ProductSerializer, TagSerializer
from .models import Product, Tag


# Product Views
class ProductListCreateAPIView(generics.ListCreateAPIView):
    """
    This endpoint returns a list of all **products** in the system.
    and allows  new products to be added.

    Only staff users have access to this endpoint.

    This endpoint allows orders to be updated.

    Only staff users can access this API.

    Fields
    id:     The product's unique identifier
    name: The name of the product
    description: A short description of the product
    tags: Product tags e.g electronics, cars etc
    regular_price: The standard product price
    sale_price: The current sale price
    weight: The products weight
    image: A sample image of the product
    inventory: Amount of a product left in store
    date: Last time product was updated
    """    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    permission_classes = [IsStaffEditorPermission]

product_list_create_view = ProductListCreateAPIView.as_view()


class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    This endpoint returns the detail of a particular product and also allows products to be edited and deleted.

    Only staff users have access to this endpoint.

    Fields
    id:     The product's unique identifier
    name: The name of the product
    description: A short description of the product
    tags: Product tags e.g electronics, cars etc
    regular_price: The standard product price
    sale_price: The current sale price
    weight: The products weight
    image: A sample image of the product
    inventory: Amount of a product left in store
    date: Last time product was updated
    """    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    permission_classes = [IsStaffEditorPermission]    

product_retrieve_update_destroy_view = ProductRetrieveUpdateDestroyView.as_view()


# Tag Views
class TagListCreateAPIView(generics.ListCreateAPIView):
    """
    This endpoint returns a list of all **tags** in the system.
    and allows  new products to be added.

    Only staff users have access to this endpoint.

    Fields
    id:     The tag's unique identifier
    name: The name or category of the tag
    image: A sample image of the tag
    """        
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    permission_classes = [IsStaffEditorPermission]    

tag_list_create_view = TagListCreateAPIView.as_view()


class TagRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    This endpoint returns the detail of a tag and also allows products to be edited and deleted.

    Only staff users have access to this endpoint.

    Fields
    id:     The tag's unique identifier
    name: The name or category of the tag
    image: A sample image of the tag
    """        
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    permission_classes = [IsStaffEditorPermission]    

tag_retrieve_update_destroy_view = TagRetrieveUpdateDestroyView.as_view()