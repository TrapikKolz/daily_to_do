from rest_framework.serializers import IntegerField, CharField, ModelSerializer

from ..notes.models import Note

class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

