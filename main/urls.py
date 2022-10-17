from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CompanyViewSet

router = DefaultRouter()
router.register('advocates', UserViewSet)
router.register('company', CompanyViewSet)

urlpatterns = router.urls