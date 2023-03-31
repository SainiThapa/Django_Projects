# Generated by Django 3.2.16 on 2023-03-30 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name',models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
                ('dest', models.TextField()),
                ('offer',models.BooleanField(default=False))
            ],
        ),
    ]
