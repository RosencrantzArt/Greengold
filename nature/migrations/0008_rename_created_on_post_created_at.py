# Generated by Django 5.1.3 on 2024-11-27 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nature', '0007_alter_post_featured_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='created_on',
            new_name='created_at',
        ),
    ]