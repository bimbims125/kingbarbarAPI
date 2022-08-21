from ninja import Router, Form

from api_v1.models import Kategori
from .schema import BaseKategoriSchema, RetrieveKategoriSchema


router = Router(tags=['Kategori'])


@router.get('/', response={200: list[RetrieveKategoriSchema]})
async def retrieve_kategori(request):
    return await Kategori.objects.async_all()


@router.get('/{slug}', response={200:list[RetrieveKategoriSchema]})
async def retrieve_kategory_by_slug(request, slug: str):
    return await Kategori.objects.async_filter(slug=slug)


@router.post('/create/')
async def create_kategori(request, payload: BaseKategoriSchema = Form(...)):
    _kategori = await Kategori.objects.async_create(**payload.dict())
    _kategori.save()
    return 200, {
        'success': True,
        'status_code': 200,
        'message': 'Data kategori berhasil dibuat',
        'data': {
            'nama': payload.nama,
            'deskripsi': payload.deskripsi
        }
    }


@router.put('/update/{id}')
async def update_kategori(request, id: int, payload: BaseKategoriSchema):
    _kategori = await Kategori.objects.async_get(id=id)
    _kategori.nama = payload.nama
    _kategori.deskripsi = payload.deskripsi
    _kategori.save()
    return 200, {
        'success': True,
        'status_code': 200,
        'message': f'Data kategori dengan id {id} berhasil diperbaharui',
    }


@router.delete('/delete/{id}')
async def delete_kategori(request, id: int):
    _kategori = await Kategori.objects.async_get(id=id)
    _kategori.delete()
    return 200, {
        'success': True,
        'status_code': 200,
        'message': f'Data kategori dengan id {id} berhasil dihapus'
    }
