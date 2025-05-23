# Generated by Django 5.2 on 2025-04-06 19:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profissional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_social', models.CharField(max_length=255)),
                ('profissao', models.CharField(max_length=255)),
                ('endereco', models.CharField(max_length=255)),
                ('contato', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField()),
                ('profissional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consultas', to='consultas.profissional')),
            ],
        ),
    ]
