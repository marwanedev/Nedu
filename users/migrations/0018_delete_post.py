# Generated by Django 4.0.4 on 2022-06-05 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_delete_extrait_remove_post_forum_post_cour_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
    ]
