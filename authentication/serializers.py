from rest_framework import serializers

from authentication.models import Image


class UserImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = (
            'custom_user_entity_id',
            'image',
        )
