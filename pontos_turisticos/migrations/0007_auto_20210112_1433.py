# Generated by Django 3.1.1 on 2021-01-12 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('localizacao', '0001_initial'),
        ('pontos_turisticos', '0006_pontoturistico_localizacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pontoturistico',
            name='localizacao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='localizacao.localizacao'),
        ),
    ]
