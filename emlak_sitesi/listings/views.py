from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Listing
from .serializers import ListingSerializer
from rest_framework.generics import RetrieveAPIView
from .models import Listing
from .serializers import ListingSerializer
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Listing
from .serializers import ListingSerializer
from rest_framework.permissions import IsAdminUser
class ListingList(APIView):
    def get(self, request):
        listings = Listing.objects.all()
        serializer = ListingSerializer(listings, many=True)
        return Response(serializer.data)

class ListingDetail(RetrieveAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

# İlan Ekleme
class ListingCreate(CreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [IsAuthenticated]  # Sadece giriş yapmış kullanıcılar
    permission_classes = [IsAdminUser]

# İlan Güncelleme
class ListingUpdate(UpdateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [IsAuthenticated]  # Sadece giriş yapmış kullanıcılar
    permission_classes = [IsAdminUser]
