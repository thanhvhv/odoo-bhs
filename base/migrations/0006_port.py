# Generated by Django 5.0.6 on 2024-07-04 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_demo_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='Port',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('port', models.IntegerField()),
            ],
        ),
    ]
