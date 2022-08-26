from ninja import Router, Form

from api_v1.models import Reseller
from api_v1.reseller.schema import BaseResellerSchema, CreateUpdateResellerSchema

router = Router(tags=['Reseller'])

@router.get('/', response={200:list[BaseResellerSchema]})
async def retrieve_reseller(request):
  return await Reseller.objects.async_all()

@router.get('/{id}', response={200:list[BaseResellerSchema]})
async def retrieve_reseller_by_id(request,id:int):
  return await Reseller.objects.async_filter(id=id)

@router.post('/create/')
async def create_reseller(request, payload:CreateUpdateResellerSchema = Form(...)):
  _reseller = await Reseller.objects.async_create(**payload.dict())
  _reseller.save()
  return 200, {
    'success':True,
    'status_code':200,
    'message':'Data reseller berhasil ditambahkan'
  }

@router.put('/update/{id}')
async def update_reseller(request, id:int, payload:CreateUpdateResellerSchema):
  _reseller = await Reseller.objects.async_get(id=id)
  _reseller.nama_toko = payload.nama_toko
  _reseller.alamat = payload.alamat
  _reseller.no_telp = payload.no_telpon
  _reseller.save()
  return 200, {
    'success':True,
    'status_code':200,
    'message':f'Data reseller dengan id {id} berhasil diperbaharui'
  }

@router.delete('/delete/{id}')
async def delete_reseller(request, id:int):
  _reseller = await Reseller.objects.get(id=id)
  _reseller.delete()
  return 200,{
    'success':True,
    'status_code':200,
    'message':f'Data reseller dengan id {id} berhasil dihapus'
  }