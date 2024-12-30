from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Group

class CreateGroupView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        group_name = request.data.get("name")
        group = Group.objects.create(name=group_name)
        group.members.add(request.user)
        return Response({"message": "Group created successfully", "group_id": group.id})

class JoinGroupView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, group_id):
        group = Group.objects.get(id=group_id)
        group.members.add(request.user)
        return Response({"message": "Joined group successfully"})

class LeaveGroupView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, group_id):
        group = Group.objects.get(id=group_id)
        group.members.remove(request.user)
        return Response({"message": "Left group successfully"})