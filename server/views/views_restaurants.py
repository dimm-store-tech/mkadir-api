from rest_framework.views import APIView
from rest_framework.response import Response
from server.model.RestaurantModel import Restaurant
from server.serializers.RestaurantSerializer import RestaurantSerializer
class getRestaurants(APIView):
    def get(self, request):
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)

class registerRestaurant(APIView):
    def post(self, request):
        serializer = RestaurantSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)