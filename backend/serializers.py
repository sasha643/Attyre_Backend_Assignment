from rest_framework import serializers
from .models import *

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id', 'name', 'logo_url']

class ProductVariantSerializer(serializers.ModelSerializer):
    options = serializers.ListField(child=serializers.CharField())

    class Meta:
        model = Variant
        fields = ['id', 'name', 'options']

class ProductSerializer(serializers.ModelSerializer):
    store = StoreSerializer()
    variants = ProductVariantSerializer(many=True)

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'price', 'original_price', 'discount_percentage', 
            'image_url', 'timestamp', 'currency', 'store', 'in_stock', 'variants'
        ]

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ['id', 'name', 'artist', 'cover_url']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'username', 'display_name', 'profile_picture_url', 
            'bio', 'followers_count', 'verified'
        ]

class VideoSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    products = ProductSerializer(many=True)
    music = MusicSerializer()

   
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if isinstance(representation['hashtags'], str):
            representation['hashtags'] = [representation['hashtags']]
        return representation

    class Meta:
        model = Video
        fields = [
            'id', 'video_url', 'thumbnail_url', 'description', 'view_count', 
            'duration', 'created_at', 'user', 'products', 'likes_count', 
            'comments_count', 'shares_count', 'is_liked', 'is_bookmarked', 
            'music', 'hashtags'
        ]
