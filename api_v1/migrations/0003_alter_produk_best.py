# Generated by Django 4.1 on 2022-08-20 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_v1', '0002_produk_best'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produk',
            name='best',
            field=models.CharField(choices=[('iya', 'iya'), ('tidak', 'tidak')], max_length=20),
        ),
    ]
