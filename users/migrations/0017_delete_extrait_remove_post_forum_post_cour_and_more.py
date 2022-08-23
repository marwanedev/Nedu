# Generated by Django 4.0.4 on 2022-06-05 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_remove_forum_posts_post_forum'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Extrait',
        ),
        migrations.RemoveField(
            model_name='post',
            name='forum',
        ),
        migrations.AddField(
            model_name='post',
            name='cour',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.cours'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Forum',
        ),
    ]
