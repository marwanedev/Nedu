# Generated by Django 4.0.4 on 2022-06-12 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0027_alter_cours_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cours',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='static/les_pdf'),
        ),
    ]
