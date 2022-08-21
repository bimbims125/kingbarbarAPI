from ninja import ModelSchema, Schema

from api_v1.models import Kategori


class RetrieveKategoriSchema(ModelSchema):
    class Config:
        model = Kategori
        model_fields = '__all__'


class BaseKategoriSchema(Schema):
    nama: str
    deskripsi: str
