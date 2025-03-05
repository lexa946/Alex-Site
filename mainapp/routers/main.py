from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from mainapp.bio import bio


router = APIRouter(prefix="", tags=['Main'])
templates = Jinja2Templates(directory="mainapp/templates")


@router.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "data": bio})
