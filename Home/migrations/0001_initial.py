# Generated by Django 4.1.7 on 2023-03-06 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WelcomePageVisitorName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitors_name', models.CharField(blank=True, default='', max_length=200, null=True)),
            ],
        ),
    ]
