from rest_framework import serializers

from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
        extra_kwargs = {
            'description': {
                # Tell DRF that the link field is not required.
                'required': False,
                'allow_blank': True,
            }
        }
