from django.contrib import admin

from .models import Kategori, Produk
# Register your models here.


class KategoriAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nama',)}


class ProdukAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nama',)}


admin.site.register(Kategori, KategoriAdmin)
admin.site.register(Produk, ProdukAdmin)
