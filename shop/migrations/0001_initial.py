# Generated by Django 4.1.1 on 2022-09-23 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='proucet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('about', models.TextField()),
                ('price', models.TextField()),
                ('image', models.ImageField(upload_to='shop_img/img/')),
            ],
        ),
    ]
