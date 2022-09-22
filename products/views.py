from rest_framework import generics

from api.permissions import IsStaffEditorPermission
from .serializers import ProductSerializer, TagSerializer
from .models import Product, Tag


# Product Views
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    permission_classes = [IsStaffEditorPermission]

product_list_create_view = ProductListCreateAPIView.as_view()


class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    permission_classes = [IsStaffEditorPermission]    

product_retrieve_update_destroy_view = ProductRetrieveUpdateDestroyView.as_view()


# Tag Views
class TagListCreateAPIView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    permission_classes = [IsStaffEditorPermission]    

tag_list_create_view = TagListCreateAPIView.as_view()


class TagRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    permission_classes = [IsStaffEditorPermission]    

tag_retrieve_update_destroy_view = TagRetrieveUpdateDestroyView.as_view()