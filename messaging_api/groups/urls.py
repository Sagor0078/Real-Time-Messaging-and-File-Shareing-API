from django.urls import path
from .views import CreateGroupView, JoinGroupView, LeaveGroupView

urlpatterns = [
    path("create/", CreateGroupView.as_view(), name="create_group"),
    path("<int:group_id>/join/", JoinGroupView.as_view(), name="join_group"),
    path("<int:group_id>/leave/", LeaveGroupView.as_view(), name="leave_group"),
]