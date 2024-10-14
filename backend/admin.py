from django.contrib import admin
from .models import User, Store, Product, Variant, Music, Video

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'display_name', 'verified', 'followers_count')

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'logo_url')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'original_price', 'in_stock', 'store')
    list_filter = ('store', 'in_stock')

@admin.register(Variant)
class VariantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'product')

@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'artist')

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'view_count', 'duration', 'created_at', 'user')
    list_filter = ('created_at', 'user')
    search_fields = ('description', 'user__username')
    date_hierarchy = 'created_at'
    filter_horizontal = ('products',)
