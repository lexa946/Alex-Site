from pydantic import BaseModel


class SWork(BaseModel):
    id: int
    name: str
    description: str | None = None
    git_url: str
    site_url: str | None = None
