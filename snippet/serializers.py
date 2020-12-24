from rest_framework import serializers
from snippet.models import SnippetModel, LANGUAGE_CHOICES, STYLES_CHOICES


# class SnippetSerializer(serializers.ModelSerializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=100, blank=True, required=False)
#     code = serializers.TextField()
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.CharField(
#         max_length=100, default='Python', choices=LANGUAGE_CHOICES)
#     style = serializers.CharField(
#         max_length=100, default='friendly', choices=STYLES_CHOICES)

#     def create(self, validated_data):
#         return SnippetModel.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = SnippetModel
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')
