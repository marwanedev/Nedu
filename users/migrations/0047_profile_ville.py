# Generated by Django 4.0.4 on 2022-06-28 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0046_profile_postblock_alter_profile_isfriend'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='ville',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]