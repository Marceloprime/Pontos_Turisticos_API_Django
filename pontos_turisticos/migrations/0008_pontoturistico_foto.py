# Generated by Django 3.1.1 on 2021-01-14 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pontos_turisticos', '0007_auto_20210112_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='pontosImages'),
        ),
    ]
