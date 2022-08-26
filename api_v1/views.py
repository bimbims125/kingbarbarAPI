from django.shortcuts import render

# Create your views here.
from ninja import NinjaAPI

from api_v1.produk.routes import router as produk_router
from api_v1.kategori.routes import router as kategori_router
from api_v1.reseller.routes import router as reseller_router

api = NinjaAPI(title='Kingbarbar API', version=1.0)

api.add_router('/produk', produk_router)
api.add_router('/kategori', kategori_router)
api.add_router('/reseller', reseller_router)