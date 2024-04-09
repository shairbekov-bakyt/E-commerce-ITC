from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from tracker.models import Task
from tracker.serializers import TaskSerializer


class TaskViewSet(GenericViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data, status=200)

    def create(self, request):
        serializer = TaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "success"})

    def destroy(self, request, pk):
        obj = Task.objects.filter(pk=pk)
        if not obj.exists():
            return Response({"message": "task not found"}, status=404)

        obj.delete()
        return Response({"message": "success deleted"})

    def partial_update(self, request, pk):
        obj = Task.objects.filter(pk=pk)
        if not obj.exists():
            return Response({"message": "task not found"}, status=404)

        serializer = TaskSerializer(data=request.data, instance=obj.first(), partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
