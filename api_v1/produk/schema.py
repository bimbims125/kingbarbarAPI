from enum import Enum
from ninja import ModelSchema, Schema
from api_v1.kategori.schema import RetrieveKategoriSchema

from api_v1.models import Kategori, Produk

class BaseProdukSchema(Schema):
    nama:str
    harga:int
    deskripsi:str
    kategori_id:int
    best:bool

class RetrieveProdukSchema(ModelSchema):
    kategori:RetrieveKategoriSchema
    class Config:
        model = Produk
        model_fields = '__all__'

class RetrieveProdukByKategoriSchema(ModelSchema):
    kategori:RetrieveKategoriSchema
    class Config:
        model = Produk
        model_fields = '__all__'