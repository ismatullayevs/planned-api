from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Todo
from .serializers import TodoSerializer
from django.contrib.auth import get_user_model
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view

User = get_user_model()


class TodoListAPIView(ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class TodoDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)


@api_view(['PATCH'])
def reorder(request, pk):
    queryset = request.user.todos.all()
    try:
        current = queryset.get(pk=pk)
    except Todo.DoesNotExist:
        raise Http404

    direction = request.GET.get('direction')
    count = int(request.GET.get('count'))

    if direction == "up":
        for i in range(count):
            current.up()
    elif direction == "down":
        for i in range(count):
            current.down();

    return Response(status=status.HTTP_204_NO_CONTENT)