# Generated by Django 4.0.4 on 2022-06-10 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0026_cours_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cours',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='les_pdf'),
        ),
    ]
