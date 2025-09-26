from oauth2_provider.contrib.rest_framework import TokenMatchesOASRequirements
from rest_framework import viewsets
from .models import Note
from .serializers import NoteSerializer

class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    permission_classes = [TokenMatchesOASRequirements]
    required_scopes = ['notes:read', 'notes:write']

    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
