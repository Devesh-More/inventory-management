from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .logger_file import logger
from rest_framework.decorators import api_view, permission_classes
from .models import Item
from .serializers import ItemSerializer
from django.core.cache import cache
from django.core.exceptions import ObjectDoesNotExist


# Create-get Item API
@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def create_item(request):
    if request.method == 'POST':
        serializer = ItemSerializer(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response({"status": True, "message": serializer.data}, status=status.HTTP_201_CREATED)
        except Exception as e:
            logger.error(f"{type(e).__name__}: {str(e)} on line number: {e.__traceback__.tb_lineno}")
        return Response({"status": False, "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    else:  
        # Fetching all the items data from the database
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response({"status": True, "message": serializer.data}, status=status.HTTP_200_OK)

# Get item by ID API and Redis caching
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_item(request, item_id):
    cache_key = f'item_{item_id}'
    item_data = cache.get(cache_key)
    
    if not item_data:
        try:
            item = Item.objects.get(id=item_id)
            serializer = ItemSerializer(item)
            item_data = serializer.data
            cache.set(cache_key, item_data)
        except Item.DoesNotExist:
            logger.error(f"Item not found: {item_id}")
            return Response({"status": False, 'message': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

    return Response({"status": True, "message": item_data})  

# Update Item API
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_item(request, item_id):
    try:
        item = Item.objects.get(id=item_id)
    except Item.DoesNotExist:
        logger.error(f"No Item found with id: {item_id}")
        return Response({'status': False, 'message': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ItemSerializer(item, data=request.data)
    if serializer.is_valid():
        serializer.save()
        cache.delete(f'item_{item_id}') 
        return Response({"status": True, "message": serializer.data})

    return Response({"status": False, "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# Delete Item API
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_item(request, item_id):
    try:
        item = Item.objects.get(id=item_id)
        item.delete()
        cache.delete(f'item_{item_id}')
        return Response({"status": True, 'message': 'Item deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except Item.DoesNotExist:
        logger.error(f"No Item found with id: {item_id}")
        return Response({"status": False, 'message': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

# Login API with JWT authentication
@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request,username=username,password=password)
    if user is not None:
        refresh = RefreshToken.for_user(user)
        return Response({"status":True,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            "message":"Login Successful"
        })
    else:
        return Response({"status":False,"message":"Incorrect user details."})


# Register API
@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')

    try:
        user = User.objects.get(username=username)
        return Response({"status": False, "message": "Username is already taken."}, status=400)
    except User.DoesNotExist:
        user = User(username=username)
        user.password = make_password(password)
        user.save()
        return Response({"status": True, "message": "User Registered Successfully."}, status=200)
    except Exception as e:
        logger.error(f"{type(e).__name__}: {str(e)} on line number: {e.__traceback__.tb_lineno}")
        return Response({"status": False, "message": "User was not registered, try again."}, status=400)