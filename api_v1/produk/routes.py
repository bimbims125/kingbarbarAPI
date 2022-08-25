from ninja import Router, Form, File
from ninja.files import UploadedFile
from imagekitio import ImageKit

from api_v1.produk.schema import BaseProdukSchema, RetrieveProdukByKategoriSchema, RetrieveProdukSchema
from api_v1.models import Produk

router = Router(tags=['Produk'])


@router.get('/', response={200: list[RetrieveProdukSchema]})
async def retrieve_produk(request):
    return await Produk.objects.async_all()


@router.get('/{int:id}', response={200: list[RetrieveProdukSchema]})
async def retrieve_produk_by_id(request, id: int):
    return await Produk.objects.async_filter(id=id)


@router.get('/{str:slug}', response={200: list[RetrieveProdukSchema]})
async def retrieve_produk_by_slug(request, slug: str):
    return await Produk.objects.async_filter(slug=slug)


@router.get('/kategori/{slug}', response={200: list[RetrieveProdukSchema]})
async def retrieve_produk_by_kategori_slug(request, slug: str):
    return await Produk.objects.async_filter(kategori__slug=slug)


@router.get('/kategori/{id}/', response={200: list[RetrieveProdukSchema]})
async def retrieve_produk_by_kategori_id(request, id: int):
    return await Produk.objects.async_filter(kategori_id=id)

@router.get('/best/{best}/', response={200: list[RetrieveProdukSchema]})
async def retrieve_best_produk(request, best:bool):
    return await Produk.objects.async_filter(best=best)

@router.post('/create/')
async def create_produk(request, payload: BaseProdukSchema = Form(...), img: UploadedFile = File(...)):
    # imagekit = ImageKit(
    #     public_key='public_DqaP16cLj4ts9XK4kFCWKmkU1j4=',
    #     private_key='private_72s6roDTx4nF0l7683JjVTEY9kw=',
    #     url_endpoint='https://ik.imagekit.io/pramdpb/'
    # )

    # upload = imagekit.upload(
    #     file=img,
    #     file_name='produk_img.jpg',
    # )
    # imageUrl = upload['response']['url']
    imgUrl = f'pram-api.herokuapp.com/media/produk/{img}'
    _produk = await Produk.objects.async_create(**payload.dict(), img=img, img_url = imgUrl)
    _produk.save()
    return 200, {
        'success': True,
        'status_code': 200,
        'message': 'Data produk berhasil dibuat',
        'data': {
            'nama': payload.nama,
            'harga': payload.deskripsi,
            'deskripsi': payload.deskripsi,
            'kategori_id': payload.kategori_id,
            'best': payload.best
        }
    }


@router.put('/update/{id}/')
async def update_produk(request, id: int, payload: BaseProdukSchema):
    _produk = await Produk.objects.async_get(id=id)
    _produk.nama = payload.nama
    _produk.harga = payload.harga
    _produk.deskripsi = payload.deskripsi
    _produk.kategori_id = payload.kategori_id
    _produk.best = payload.best
    _produk.save()
    return {
        'success': True,
        'status_code': 200,
        'message': f'Data produk dengan id {id} berhasil di perbaharui'
    }


@router.delete('/delete/{id}')
async def delete_produk(request, id: int):
    _produk = await Produk.objects.async_get(id=id)
    _produk.delete()
    return 200, {
        'success': True,
        'status_code': 200,
        'message': f'Data Produk dengan id {id} berhasil dihapus'
    }
