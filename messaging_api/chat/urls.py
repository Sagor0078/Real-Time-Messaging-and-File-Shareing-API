from django.urls import path
from .views import RetrieveMessagesView

urlpatterns = [
    path("messages/<int:conversation_id>/", RetrieveMessagesView.as_view(), name="retrieve_messages"),
]
