# Generated by Django 4.0.4 on 2022-06-18 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0029_domaine_counter_alter_paragraphe_titre_paragraphe'),
    ]

    operations = [
        migrations.AddField(
            model_name='cours',
            name='counter',
            field=models.IntegerField(default=0),
        ),
    ]
