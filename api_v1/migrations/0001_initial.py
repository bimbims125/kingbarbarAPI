# Generated by Django 4.1 on 2022-08-20 00:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('deskripsi', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Produk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=55)),
                ('slug', models.SlugField()),
                ('deskripsi', models.TextField()),
                ('harga', models.PositiveIntegerField()),
                ('img', models.URLField()),
                ('kategori', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api_v1.kategori')),
            ],
        ),
    ]