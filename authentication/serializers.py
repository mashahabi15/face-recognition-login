from rest_framework import serializers

from authentication.models import ImageEntity


class UserImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageEntity
        fields = (
            'custom_user_entity',
            'image',
        )
