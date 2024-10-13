from rest_framework import serializers
from apps.notes.models import Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        read_only_fields = (
            "id",
            "created_at",
            "created_by",
        )

        fileds = (
            "id", 
            "created_at",
            "created_by",
            "content"
        )
