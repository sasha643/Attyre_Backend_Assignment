# Generated by Django 5.1.2 on 2024-10-14 18:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Music",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("artist", models.CharField(max_length=255)),
                ("cover_url", models.URLField()),
            ],
            options={
                "indexes": [
                    models.Index(
                        fields=["name", "artist"], name="backend_mus_name_763c0d_idx"
                    )
                ],
            },
        ),
        migrations.CreateModel(
            name="Store",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                ("logo_url", models.URLField()),
            ],
            options={
                "indexes": [
                    models.Index(fields=["name"], name="backend_sto_name_9a39eb_idx")
                ],
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "original_price",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                (
                    "discount_percentage",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                ("image_url", models.URLField()),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("currency", models.CharField(max_length=3)),
                ("in_stock", models.BooleanField(default=True)),
                (
                    "store",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products",
                        to="backend.store",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("username", models.CharField(max_length=255, unique=True)),
                ("display_name", models.CharField(max_length=255)),
                ("profile_picture_url", models.URLField()),
                ("bio", models.TextField(blank=True)),
                ("followers_count", models.PositiveIntegerField(default=0)),
                ("verified", models.BooleanField(default=False)),
            ],
            options={
                "indexes": [
                    models.Index(
                        fields=["username"], name="backend_use_usernam_127560_idx"
                    ),
                    models.Index(
                        fields=["followers_count"],
                        name="backend_use_followe_5eb55e_idx",
                    ),
                ],
            },
        ),
        migrations.CreateModel(
            name="Variant",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("options", models.JSONField()),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="variants",
                        to="backend.product",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Video",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("video_url", models.URLField()),
                ("thumbnail_url", models.URLField()),
                ("description", models.TextField(blank=True)),
                ("view_count", models.PositiveIntegerField(default=0)),
                ("duration", models.PositiveIntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("likes_count", models.PositiveIntegerField(default=0)),
                ("comments_count", models.PositiveIntegerField(default=0)),
                ("shares_count", models.PositiveIntegerField(default=0)),
                ("is_liked", models.BooleanField(default=False)),
                ("is_bookmarked", models.BooleanField(default=False)),
                ("hashtags", models.JSONField(blank=True, default=list)),
                (
                    "music",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="videos",
                        to="backend.music",
                    ),
                ),
                (
                    "products",
                    models.ManyToManyField(related_name="videos", to="backend.product"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="videos",
                        to="backend.user",
                    ),
                ),
            ],
        ),
        migrations.AddIndex(
            model_name="product",
            index=models.Index(
                fields=["name", "store"], name="backend_pro_name_9bd22b_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="video",
            index=models.Index(
                fields=["created_at"], name="backend_vid_created_686cd7_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="video",
            index=models.Index(fields=["user"], name="backend_vid_user_id_83be30_idx"),
        ),
    ]
