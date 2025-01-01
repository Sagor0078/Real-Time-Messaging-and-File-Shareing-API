from django.db import models
from django.utils.timezone import now, timedelta
from users.models import User
from groups.models import Group

def default_file_expiry():
    return now() + timedelta(days=10)

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")
    receiver_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="received_messages")
    receiver_group = models.ForeignKey(Group, null=True, blank=True, on_delete=models.CASCADE, related_name="group_messages")
    message = models.CharField(max_length=255, null=True, blank=True)
    file = models.FileField(upload_to="uploads/", null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    file_expiry = models.DateTimeField(default=default_file_expiry)