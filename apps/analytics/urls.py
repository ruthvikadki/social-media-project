from django.urls import path
from .views import AnalyticsView, AnalyticsAPIView

app_name = "analytics"

urlpatterns = [
    path('', AnalyticsView.as_view(), name='home'),
    path('api/chart_data/', AnalyticsAPIView.as_view(), name='api'),
]
