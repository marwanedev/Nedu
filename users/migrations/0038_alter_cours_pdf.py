# Generated by Django 4.0.4 on 2022-06-21 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0037_remove_friend_profile_remove_profile_friends_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cours',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='PDFs'),
        ),
    ]
