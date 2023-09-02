from rest_framework import serializers
from .models import *

class PenisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('name', 'content_mockup', 'category',)

    def create(self, validated_data):
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.content_mockup = validated_data.get('content_mockup', instance.content_mockup)
        instance.category = validated_data.get('category', instance.category)
        instance.datetime_created = validated_data.get('datetime_created', instance.datetime_created)
        instance.datetime_updated = validated_data.get('datetime_updated', instance.datetime_updated)
        instance.save()
        return instance

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('name', 'content_mockup', 'category')

    def create(self, validated_data):
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.content_mockup = validated_data.get('content_mockup', instance.content_mockup)
        instance.category = validated_data.get('category', instance.category)
        instance.datetime_created = validated_data.get('datetime_created', instance.datetime_created)
        instance.datetime_updated = validated_data.get('datetime_updated', instance.datetime_updated)
        instance.save()
        return instance

class CategorySerializer(serializers.Serializer):
    name = serializers.CharField()

    def create(self, validated_data):
        return CategoryArticle.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance















    # def create(self, validated_data):
    #     return Article.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.content_mockup = validated_data.get('content_mockup', instance.content_mockup)
    #     instance.category = validated_data.get('category', instance.category)
    #     instance.datetime_created = validated_data.get('datetime_created', instance.datetime_created)
    #     instance.datetime_updated = validated_data.get('datetime_updated', instance.datetime_updated)
    #     instance.save()
    #     return instance

















#-------------------------------------------

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('name', 'content_mockup', 'category')

class ArticleTestSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    content_mockup = serializers.CharField()
    category_id = serializers.IntegerField()

# class TestSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=255)
#     category_id = serializers.IntegerField()
#     content_mockup = serializers.CharField()
#
# class Test:
#     def __init__(self, name, cat_id, cont_mup):
#         self.name = name
#         self.category_id = cat_id
#         self.content_mockup = cont_mup
