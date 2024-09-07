from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from mainapp.backend.db import get_db
from mainapp.models import WorkOrm
from mainapp.schemas import SWork

router = APIRouter(prefix='/works', tags=['Работы'])


@router.get('/')
async def get_all_works(db: Annotated[AsyncSession, Depends(get_db)]) -> list[SWork]:
    works = await db.scalars(
        select(WorkOrm)
    )
    works = works.all()
    works = [SWork.model_validate({
        "id": work.id, "name": work.name, "description": work.description,
        "git_url": work.git_url, "site_url":work.site_url
    }) for work in works]
    return works
