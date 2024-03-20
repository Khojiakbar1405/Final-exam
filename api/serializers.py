
from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework import serializers
from main import models 


# Products Serializer
class ListProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    class Meta:
        model = models.Product
        fields = '__all__'
        # fields = ['name', 'title', 'category', 'quantity', 'price', 'image', ]



# Create Product Serializer
class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ['name', 'title', 'category', 'quantity', 'price', 'image', ]



# Detail Product Serializer
class DetailProductSerilaizer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    class Meta:
        model = models.Product
        depth = 1
        fields = ['id', 'name', 'title', 'price',
                   'quantity', 'discount_price',
                    'image', 'category',
                    'is_discount', 'is_active',]



# Delete Product Serializer
class DeleteProductView(DestroyAPIView):
    queryset = models.Product.objects.all()
    serializer_class = ListProductSerializer



# List Category Serializer
class ListCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'
        depth = 1



class DetailCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ['name', ]
        depth = 1



# Create Category Serializer
class CreateCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ['name', ]



# Delete Category
class DeleteCategoryView(DestroyAPIView):
    queryset = models.Category.objects.all()
    serializer_class = ListCategorySerializer



# List Cart Serializer
class ListCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cart
        fields = '__all__'



# Create Cart Serializer
class CreateCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cart
        fields = ['user', 'is_active', ]



# List Cart Product Serializer
class ListCartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CartProduct
        fields = '__all__'



#  Create Cart Product Serializer
class CreateCartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CartProduct
        fields = ['cart', 'product', 'quantity', ]



# Detail Cart Product Serializer
class DetailCartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CartProduct
        fields = ['cart', 'product', 'quantity', 'total_price', ]



# Delete Cart Product
class DeleteCartProductView(DestroyAPIView):
    queryset = models.CartProduct.objects.all()
    serializer_class = ListCartProductSerializer



# Order List Serialiser
class ListOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = '__all__'



# Order Detail Serializer
class DetailOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = ['user', 'cart', 'created', 'status', 'total_price']



# Order Create Serializer
class CreateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = ['user', 'cart', 'status',]



# Order Delete 
class DeleteOrderView(DestroyAPIView):
    queryset = models.Order.objects.all()
    serializer_class = ListOrderSerializer
    

# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'