from cgi import print_form

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
from django.shortcuts import render, get_object_or_404, redirect
from .models import Listing


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

def home(request):
    listings = Listing.objects.all()
    return render(request, 'home.html', {'listings': listings})

def listing_detail(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    return render(request, 'listing_detail.html', {'listing': listing})

<<<<<<< Updated upstream
=======
def search_view(request):
    query = request.GET.get('q')
    if query:
        results = Listing.objects.filter(name__icontains=query)

def arsa(request):
    arsa_listesi = Listing.objects.filter(type='arsa')# 'kategori' field'ını arsa olanları alıyoruz
    return render(request, 'arsa.html', {'arsalar': arsa_listesi})

def ev(request):
    ev_listesi = Listing.objects.filter(type='ev')# 'kategori' field'ını arsa olanları alıyoruz
    return render(request, 'ev.html', {'evler': ev_listesi})

def tarla(request):
    tarla_listesi = Listing.objects.filter(type='tarla')
    return render(request, 'tarla.html', {'tarlalar': tarla_listesi})

>>>>>>> Stashed changes
def add_listing(request):
    if request.method == 'POST':
        title = request.POST['title']
        price = request.POST['price']
        type = request.POST['type']
        description = request.POST['description']
        contact_number = request.POST['contact_number']
        Listing.objects.create(
            title=title,
            price=price,
            type=type,
            description=description,
            contact_number=contact_number,
        )
        return redirect('home')
    return render(request, 'add_listing.html')