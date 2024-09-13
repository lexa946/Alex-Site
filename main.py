from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from mainapp.routers import main

app = FastAPI()
app.include_router(main.router)
app.mount('/static/main', StaticFiles(directory='mainapp/static'), 'main_static')

#TODO: переделай хранение проектов на посгрю