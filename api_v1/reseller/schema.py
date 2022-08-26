from ninja import Schema, ModelSchema
from api_v1.models import Reseller

class BaseResellerSchema(ModelSchema):
  class Config:
    model = Reseller
    model_fields = '__all__'

class CreateUpdateResellerSchema(Schema):
  nama_toko:str
  alamat:str
  no_telpon:int