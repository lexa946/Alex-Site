from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.trustedhost import TrustedHostMiddleware
from uvicorn.middleware.proxy_headers import ProxyHeadersMiddleware

from mainapp.routers.main import router as main_router

# app = FastAPI()
app = FastAPI(root_path="https://site.pozhar.keenetic.pro")
app.mount('/static', StaticFiles(directory='mainapp/static'), 'main_static')
app.include_router(main_router)

app.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"])
app.add_middleware(ProxyHeadersMiddleware)