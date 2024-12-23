from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .serializers import UserLoginSerializer
from .serializers import UserRegistrationSerializer
from .models.task import Task
from .serializers import TaskSerializer
from .models.tag import Tag
from .serializers import TagSerializer

class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]  # Allow unauthenticated users

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Registration successful"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [permissions.AllowAny]  # Allow unauthenticated users
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# List and Create Tasks
class TaskPagination(PageNumberPagination):
    page_size = 10  # Number of tasks per page
    page_size_query_param = 'page_size'  # Allow clients to set page size
    max_page_size = 50  # Maximum limit for page size

class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = TaskPagination  # Enable pagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]  # Enable filtering and sorting
    filterset_fields = ['status', 'tags', 'parent_task']  # Fields to filter by
    ordering_fields = ['due_date', 'created_at']  # Fields to sort by
    ordering = ['due_date']  # Default ordering

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        # Automatically set the logged-in user as the task's owner
        serializer.save(user=self.request.user)

# Retrieve, Update, and Delete a Task
class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Restrict access to tasks belonging to the logged-in user
        return Task.objects.filter(user=self.request.user)
    

class TagListCreateView(generics.ListCreateAPIView):
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Fetch only tags created by the logged-in user
        return Tag.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        # Assign the logged-in user as the tag creator
        serializer.save(created_by=self.request.user)



class TagDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Fetch only tags created by the logged-in user
        return Tag.objects.filter(created_by=self.request.user)
