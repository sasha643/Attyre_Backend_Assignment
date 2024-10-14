from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255, unique=True)  # Ensure usernames are unique
    display_name = models.CharField(max_length=255)
    profile_picture_url = models.URLField()
    bio = models.TextField(blank=True)  # Allow blank bios
    followers_count = models.PositiveIntegerField(default=0)  # Use PositiveIntegerField for counts
    verified = models.BooleanField(default=False)

    class Meta:
        indexes = [
            models.Index(fields=['username']),
            models.Index(fields=['followers_count']),
        ]

class Store(models.Model):
    name = models.CharField(max_length=255, unique=True)  # Ensure store names are unique
    logo_url = models.URLField()

    class Meta:
        indexes = [
            models.Index(fields=['name']),
        ]

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Allow null if no discount
    image_url = models.URLField()
    timestamp = models.DateTimeField(auto_now_add=True)  # Use DateTimeField for better time management
    currency = models.CharField(max_length=3)
    store = models.ForeignKey(Store, related_name='products', on_delete=models.CASCADE)
    in_stock = models.BooleanField(default=True)

    class Meta:
        indexes = [
            models.Index(fields=['name', 'store']),
        ]

class Variant(models.Model):
    product = models.ForeignKey(Product, related_name='variants', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    options = models.JSONField()

class Music(models.Model):
    name = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    cover_url = models.URLField()

    class Meta:
        indexes = [
            models.Index(fields=['name', 'artist']),
        ]

class Video(models.Model):
    video_url = models.URLField()
    thumbnail_url = models.URLField()
    description = models.TextField(blank=True)  # Allow blank descriptions
    view_count = models.PositiveIntegerField(default=0)  # Use PositiveIntegerField for counts
    duration = models.PositiveIntegerField()  # Use PositiveIntegerField for duration
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the timestamp
    user = models.ForeignKey(User, related_name='videos', on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name='videos')
    likes_count = models.PositiveIntegerField(default=0)  # Use PositiveIntegerField for counts
    comments_count = models.PositiveIntegerField(default=0)  # Use PositiveIntegerField for counts
    shares_count = models.PositiveIntegerField(default=0)  # Use PositiveIntegerField for counts
    is_liked = models.BooleanField(default=False)
    is_bookmarked = models.BooleanField(default=False)
    music = models.ForeignKey(Music, related_name='videos', on_delete=models.CASCADE, null=True, blank=True)
    hashtags = models.JSONField(blank=True, default=list)  # Allow blank hashtags with a default empty list

    class Meta:
        indexes = [
            models.Index(fields=['created_at']),
            models.Index(fields=['user']),
        ]
