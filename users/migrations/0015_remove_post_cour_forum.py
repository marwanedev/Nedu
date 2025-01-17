# Generated by Django 4.0.4 on 2022-06-05 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_remove_cours_forum_post_cour'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='cour',
        ),
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cour', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.cours')),
                ('posts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.post')),
            ],
        ),
    ]
