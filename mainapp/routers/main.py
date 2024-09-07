from typing import Annotated

from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.ext.asyncio import AsyncSession

from mainapp.backend.db import get_db
from mainapp.routers.works import get_all_works

router = APIRouter(prefix="/main", tags=['Main'])
templates = Jinja2Templates(directory="mainapp/templates")


@router.get('/')
async def index(db: Annotated[AsyncSession, Depends(get_db)], request: Request) -> HTMLResponse:
    works = await get_all_works(db)

    return templates.TemplateResponse(r"index.html", {
        "request": request, "works": works,
    })
