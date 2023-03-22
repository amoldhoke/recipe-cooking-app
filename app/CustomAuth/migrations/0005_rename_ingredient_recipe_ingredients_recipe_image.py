# Generated by Django 4.1.7 on 2023-03-19 14:19

import CustomAuth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomAuth', '0004_ingredient_recipe_ingredient'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='ingredient',
            new_name='ingredients',
        ),
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(null=True, upload_to=CustomAuth.models.recipe_image_file_path),
        ),
    ]