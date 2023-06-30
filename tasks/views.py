from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from tasks.models import Tasks
from tasks.serializers import TasksSerializer


class TasksViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer

    @action(detail=True, methods=["PUT"])
    def complete(self, request, pk):
        task = self.get_object()

        if task.completed:
            return Response(status=400, data={"error": "task is already completed"})

        task.completed = True
        task.save()

        return Response(TasksSerializer(task).data)
