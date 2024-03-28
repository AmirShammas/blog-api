# Generated by Django 4.2 on 2024-03-28 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0005_alter_category_options_alter_comment_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="category",
            field=models.ForeignKey(
                default=4,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="posts",
                to="posts.category",
                verbose_name="Category",
            ),
        ),
    ]
