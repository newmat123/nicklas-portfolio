# Generated by Django 3.2.5 on 2021-07-26 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imgs',
            name='img',
            field=models.ImageField(upload_to='langs/'),
        ),
    ]
