from sqlalchemy.orm import Mapped, mapped_column

from mainapp.backend.db import Base


class WorkOrm(Base):
    __tablename__ = "works"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str]
    description: Mapped[str | None] = mapped_column(default=None)
    git_url: Mapped[str] = mapped_column(unique=True)
    site_url: Mapped[str | None] = mapped_column(default=None)
