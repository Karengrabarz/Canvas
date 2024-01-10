from rest_framework import serializers
from .models import Content

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['id', 'name', 'content', 'video_url']
        read_only_fields = ['id']
        extra_kwargs = {
            'course':{'read_only':True},
            'video_url':{'allow_blank':True}
        }
    def update(self, instance, validated_data):
        for k, v in validated_data.items():
            if k != "content":
                continue
            setattr(instance, k, v)
        instance.save()
        return instance
    
