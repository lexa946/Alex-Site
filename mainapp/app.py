
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.httpsredirect import HTTPSRedirectMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware

from mainapp.routers.main import router as main_router

app = FastAPI()
app.mount('/static', StaticFiles(directory='mainapp/static'), 'main_static')
app.include_router(main_router)

app.add_middleware(HTTPSRedirectMiddleware)  # Перенаправляет HTTP на HTTPS
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["site.pozhar.keenetic.pro"]
)