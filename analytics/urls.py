# analytics/urls.py
from rest_framework.routers import DefaultRouter
from .views import TheaterViewSet, MovieViewSet, TicketSaleViewSet


router = DefaultRouter()
router.register('theaters', TheaterViewSet)
router.register('movies', MovieViewSet)
router.register('ticket-sales', TicketSaleViewSet)


urlpatterns = router.urls