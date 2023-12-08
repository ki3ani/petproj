from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from kimscon.views import ProductViewSet, OrderViewSet, ReviewViewSet, AnalyticsViewSet
from django.contrib.auth import views as auth_views
from kimscon import views

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'analytics', AnalyticsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='kimscon/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='kimscon/logout.html'), name='logout'),


]