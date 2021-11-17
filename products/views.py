from products.models import Product
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from products.serializers import ProductSerializer
from rest_framework.authentication import TokenAuthentication
from  rest_framework.permissions import IsAuthenticated



class ProductView(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )


    def get(self, request, *args, **kwargs):
        product_queryset = Product.objects.all() # querying all products present in database

        serializer = ProductSerializer(product_queryset, many=True) # serializing these product objects in JSON format

        return Response({
            'status': True,
            'message': 'Products fetched successfully.',
            'data': serializer.data
        }, status=status.HTTP_200_OK)



    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data, context={'request': request})

        if serializer.is_valid(): # checking if product data provided by the user is valid
            serializer.save() # creating a product in database

            # returning success response to user.
            return Response({ 
                'status': True,
                'message': 'Product created successfully.', 
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
            
        else:
            # returning error message to user.
            return Response({
                'status': False,
                'message': serializer.errors,
                'data': None
            }, status=status.HTTP_400_BAD_REQUEST)



    def put(self, request, *args, **kwargs):
        product_id = request.data.get('id') # grabing id of product need to be updated, from the request body

        try:
            obj = Product.objects.get(id=product_id) # grabing desired product from database
        except:
            # returning error message if id is invalid
            return Response({
                'status': False,
                'message': 'Void or Invalid id for product.',
                'data': None
            }, status=status.HTTP_400_BAD_REQUEST)

 
        serializer = ProductSerializer(obj, data=request.data, context={'request': request}, partial=True)

        if serializer.is_valid(): # checking if provided data is valid
            serializer.save() # updating product with provided data

            # returning success response to user
            return Response({
                'status': True,
                'message': 'Product updated successfully.',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
            
        
        else:
            # returinig error message to user
            return Response({
                'status': False,
                'message': serializer.errors,
                'data': None
            }, status=status.HTTP_400_BAD_REQUEST)



    def delete(self, request, *args, **kwargs):
        product_id = self.request.query_params.get('id') # grabing id of product need to be deleted, from the URL params

        try:
            obj = Product.objects.get(id=product_id) # grabing desired product from database
        except:
            # returning error message if id is invalid or void
            return Response({
                'status': False,
                'message': 'Void or Invalid id for product.',
                'data': None
            }, status=status.HTTP_400_BAD_REQUEST)

        serializer = ProductSerializer(obj)
        obj.delete() # deleting product object from database

        # returning success response to user
        return Response({
            'status': True,
            'message': 'Product deleted successfully.',
            'data': serializer.data
        }, status=status.HTTP_200_OK)

            