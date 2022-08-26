from distutils.command.upload import upload
from django.db import models
from django.utils.text import slugify
# Create your models here.


class Kategori(models.Model):
    nama = models.CharField(max_length=50, blank=False)
    slug = models.SlugField()
    deskripsi = models.TextField()

    def __str__(self) -> str:
        return self.nama

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nama)
        super(Kategori, self).save()

class Produk(models.Model):
    BEST_CHOICES = [
        ('iya','iya'),
        ('tidak','tidak')
    ]
    nama = models.CharField(max_length=55, blank=False)
    slug = models.SlugField()
    deskripsi = models.TextField()
    harga = models.PositiveIntegerField()
    kategori = models.ForeignKey(
        Kategori, on_delete=models.SET_NULL, null=True)
    img = models.FileField(upload_to = 'produk/')
    img_url = models.URLField()
    def __str__(self) -> str:
        return self.nama

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nama)
        super(Produk, self).save()

class Reseller(models.Model):
    nama_toko = models.CharField(max_length=100, blank=False)
    alamat = models.TextField()
    no_telpon = models.PositiveIntegerField()