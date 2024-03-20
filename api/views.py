from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from . import serializers
from main import models

from rest_framework.permissions import IsAuthenticated
from rest_framework import authentication
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authtoken.models import Token

"""
Login User
1) user token: 7d34cd284ba6cd8410493be8bff65a4aa90f78b5   username:1  password:1
3) user token: 9faa69750ec390293f77cbdfa71e739761fe255d   username:3  password:3
"""



# Product list
@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
def products_list(request):
    products = models.Product.objects.all()
    serializer = serializers.ListProductSerializer(products, many=True)
    return Response(serializer.data)



# Product create
@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
def product_create(request):
    if request.method == 'POST':
            name = request.data['name']
            title = request.data['title']
            category_id = request.data['category']
            quantity = request.data['quantity']
            price = request.data['price']
            image = request.data['image']
            category = models.Category.objects.get(id = category_id)
            models.Product.objects.create(
                name=name,
                title=title,
                category=category,
                quantity=quantity,
                price=price,
                image=image
            )
            return Response({'create': 'success'}, status=status.HTTP_201_CREATED)
    return Response({'create': 'error'}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['PUT'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
def product_update(request, id):
    try:
        name = request.data['name']
        title = request.data['title']
        category_id = request.data['category']
        quantity = request.data['quantity']
        price = request.data['price']
        image = request.data['image']
        category = models.Category.objects.get(id = category_id)
        product = models.Product.objects.get(id = id)
        product.name=name
        product.title=title
        product.category=category
        product.quantity=quantity
        product.price=price
        product.image=image
        product.save()
        return Response({'update': 'success'}, status=status.HTTP_200_OK)
    except:
        return Response({'update': 'error'}, status=status.HTTP_400_BAD_REQUEST)


            
# Product detail
@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
def product_detail(request, id):
    product = models.Product.objects.get(id=id)
    product_ser = serializers.DetailProductSerilaizer(product)
    return Response(product_ser.data)



# Product delete
@api_view(['DELETE'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
def product_delete(request, id):
    try:
        product = models.Product.objects.get(id=id)
    except models.Product.DoesNotExist:
        return Response({'error':'Not found'},status=status.HTTP_404_NOT_FOUND)
    product.delete()
    return Response({'success':'delete'},status=status.HTTP_200_OK)



# Category list
@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
def category_list(request):
    categorys = models.Category.objects.all()
    serializer = serializers.ListCategorySerializer(categorys, many=True)
    return Response(serializer.data)



# Category create
@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
def category_create(request):
    if request.method == 'POST':
        name = request.data['name']
        models.Category.objects.create(
            name=name,
        )
        return Response({'create': 'success'}, status=status.HTTP_201_CREATED)
    return Response({'create': 'error'}, status=status.HTTP_400_BAD_REQUEST)


# Category update
@api_view(['PUT'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
def category_update(request, id):
    try:
        name = request.data['name']
        category = models.Category.objects.get(id = id)
        category.name = name
        category.save()
        return Response({'update': 'success'}, status=status.HTTP_200_OK)
    except:
        return Response({'update': 'error'}, status=status.HTTP_400_BAD_REQUEST)



# Category detail
@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
def category_detail(request, id):
    category = models.Category.objects.get(id=id)
    serializer = serializers.DetailCategorySerializer(category)
    return Response(serializer.data)



# Category delete
@api_view(['DELETE'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
def category_delete(request, id):
    try:
        category = models.Category.objects.get(id=id)
    except models.Category.DoesNotExist:
        return Response({'error':'delete'}, status=status.HTTP_404_NOT_FOUND)
    category.delete()
    return Response({'success':'delete'},status=status.HTTP_200_OK)



# Cart list
@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
def cart_list(request):
    cart = models.Cart.objects.all()
    serializer = serializers.ListCartSerializer(cart, many=True)
    return Response(serializer.data)



# Cart create
@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
def cart_create(request):
    if request.method == 'POST':
        user_id = request.data['user']
        is_active = request.data['is_active']
        user = models.User.objects.get(id=user_id)
        models.Cart.objects.create(
            user=user,
            is_active=is_active,
        )
        return Response({'create': 'success'}, status=status.HTTP_201_CREATED)
    return Response({'create': 'error'}, status=status.HTTP_400_BAD_REQUEST)



# Cart delete
@api_view(['DELETE'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
def cart_delete(request, id):
    try:
        cart = models.Cart.objects.get(id=id)
    except models.Cart.DoesNotExist:
        return Response({'error':'delete'}, status=status.HTTP_404_NOT_FOUND)
    cart.delete()
    return Response({'success':'delete'}, status=status.HTTP_200_OK)



# Cart Product list
@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
def cart_product_list(request):
    cart_product = models.CartProduct.objects.all()
    serializer = serializers.ListCartProductSerializer(cart_product, many=True)
    return Response(serializer.data)



# Cart Product create
@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
def cart_product_create(request):
    if request.method == 'POST':
        cart_id = request.data['cart']
        product_id = request.data['product']
        quantity = request.data['quantity']
        cart = models.Cart.objects.get(id = cart_id)
        product = models.Product.objects.get(id = product_id)
        models.CartProduct.objects.create(
            cart=cart,
            product=product,
            quantity=quantity
        )
        return Response({'create': 'success'}, status=status.HTTP_201_CREATED)
    return Response({'create': 'error'}, status=status.HTTP_400_BAD_REQUEST)



# Cart Product detail
@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
def cart_product_detail(request, id):
    product = models.CartProduct.objects.get(id=id)
    serializer = serializers.DetailCartProductSerializer(product)
    return Response(serializer.data)



# Cart Product delete
@api_view(['DELETE'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
def cart_product_delete(request, id):
    try:
        cart_product = models.CartProduct.objects.get(id=id)
    except models.CartProduct.DoesNotExist:
        return Response({'error':'delete'}, status=status.HTTP_404_NOT_FOUND)
    cart_product.delete()
    return Response({'success':'delete'}, status=status.HTTP_200_OK)



# Order list
@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
def order_list(request):
    order = models.Order.objects.all()
    serializer = serializers.ListOrderSerializer(order, many=True)
    return Response(serializer.data)



# Order create
@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
def order_create(request):
    if request.method == 'POST':
        user_id = request.data['user']
        cart_id = request.data['cart']
        status = request.data['status']
        user = models.User.objects.get(id = user_id)
        cart = models.Cart.objects.get(id = cart_id)
        models.Order.objects.create(
            user=user,
            cart=cart,
            status=status
        )
        return Response({'create': 'success'})
    return Response({'create': 'error'})



# Order update
@api_view(['PUT'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
def order_update(request, id):
    try:
        user_id = request.data['user']
        cart_id = request.data['cart']
        status = request.data['status']
        user = models.User.objects.get(id = user_id)
        cart = models.Cart.objects.get(id = cart_id)
        order = models.Order.objects.get(id = id)
        order.user=user
        order.cart=cart
        order.status=status
        order.save()
        return Response({'update': 'success'})
    except:
        return Response({'update': 'error'})



# Order detail
@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
def order_detail(request,id):
    order = models.Order.objects.get(id=id)
    serializer = serializers.DetailOrderSerializer(order)
    return Response(serializer.data)



# Order delete
@api_view(['DELETE'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
def order_delete(request, id):
    try:
        order = models.Order.objects.get(id=id)
    except models.Order.DoesNotExist:
        return Response({'error':'delete'}, status=status.HTTP_404_NOT_FOUND)
    order.delete()
    return Response({'success':'delete'}, status=status.HTTP_200_OK)



# Login
@api_view(['POST'])
def login(request):
    username = request.data['username']
    password = request.data['password']
    user = authenticate(username = username, password = password)
    if user is not None:
        token, _ = Token.objects.get_or_create(user = user)
        info = {
            'token': token.key
        }
    else:
        info = {'fatal':'user not found'}
    return Response(info)



# Register
@api_view(['POST'])
def register(request):
    username = request.data['username']
    password = request.data['password']
    confirm_password = request.data['confirm_password']
    if models.User.objects.filter(username = username).first():
        return Response({'error':'user registered'})
    elif password == confirm_password:
        user = models.User.objects.create_user(
            username = username,
            password = password
        )
        user_ser = serializers.UserSerializer(user)
        token, _ = Token.objects.get_or_create(user = user)
        data = {
            'token': token.key,
            'user': user_ser.data
        }
        return Response(data)
    else:
        return Response({'error':'check the password'})



# Logout
@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout(request):
    request.user.auth_token.delete()
    return Response({'success':'logged out succesfully'})
