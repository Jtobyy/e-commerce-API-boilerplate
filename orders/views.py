from rest_framework import generics, status, permissions
from rest_framework.response import Response

from .mixins import StaffGetsAllOrderMixin, StaffGetsAllPaymentMixin
from .serializers import OrderSerializer, PaymentSerializer
from api.permissions import IsStaffEditorPermission


# Order Views
class OrderListCreateView(StaffGetsAllOrderMixin, generics.ListCreateAPIView):    
    serializer_class = OrderSerializer

    # Link any new order to the current logged in user
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)

    permission_classes = [permissions.IsAuthenticated]

order_list_create_view = OrderListCreateView.as_view()


class OrderUpdateView(StaffGetsAllOrderMixin, generics.UpdateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsStaffEditorPermission]

order_update_view = OrderUpdateView.as_view()


class OrderRetrieveView(StaffGetsAllOrderMixin, generics.RetrieveAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]    

order_retrieve_view = OrderRetrieveView.as_view()



# Payment Views
class PaymentListCreateView(StaffGetsAllPaymentMixin, generics.ListCreateAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # Validates payment
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.request.user
        order = serializer.validated_data.get('order')
        if order.user == user:
            serializer.save(user=user)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({'message': 'This order is not yours'}, status=status.HTTP_406_NOT_ACCEPTABLE)

payment_list_create_view = PaymentListCreateView.as_view()


class PaymentUpdateView(StaffGetsAllPaymentMixin, generics.UpdateAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [IsStaffEditorPermission]

payment_update_view = PaymentUpdateView.as_view()


class PaymentRetrieveView(StaffGetsAllPaymentMixin, generics.RetrieveAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

payment_retrieve_view = PaymentRetrieveView.as_view()