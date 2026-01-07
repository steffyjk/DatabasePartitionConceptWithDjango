# analytics/views.py
from rest_framework.viewsets import ModelViewSet
from .models import Theater, Movie, TicketSale
from .serializers import TheaterSerializer, MovieSerializer, TicketSaleSerializer


class TheaterViewSet(ModelViewSet):
    queryset = Theater.objects.all()
    serializer_class = TheaterSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class TicketSaleViewSet(ModelViewSet):
    queryset = TicketSale.objects.all()
    serializer_class = TicketSaleSerializer