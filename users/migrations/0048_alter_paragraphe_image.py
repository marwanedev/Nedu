# Generated by Django 4.0.4 on 2022-06-29 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0047_profile_ville'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paragraphe',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='photos'),
        ),
    ]
