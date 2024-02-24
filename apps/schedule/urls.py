from django.urls import path
from .views import SchedulePostCreateView, SchedulePostListView, SchedulePostDetailView


app_name = "schedule"

urlpatterns = [
    path('schedule_page/', SchedulePostListView.as_view(), name = "schedule_page"),
    path('schedule_page/create_schedule/', SchedulePostCreateView.as_view(), name = "schedule_create"),
    path('schedule/detail/<int:id>/', SchedulePostDetailView.as_view(), name = "schedule_detail")
]