from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from mainapp.routers.main import router as main_router

app = FastAPI()
app.mount('/static', StaticFiles(directory='mainapp/static'), 'main_static')
app.include_router(main_router)