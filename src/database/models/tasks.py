from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Text, Boolean
from src.database.base import Base
from pydantic import BaseModel
from typing import Optional


class Task(Base):
    title: Mapped[str] = mapped_column(String(length=1024))
    description: Mapped[str] = mapped_column(Text())
    media_url: Mapped[str] = mapped_column(String(length=1024))
    is_done: Mapped[bool] = mapped_column(Boolean, default=False)

    def to_read_model(self):
        return TasksModel(
            pk=self.pk,
            title=self.title,
            description=self.description,
            media_url=self.media_url,
            is_done=self.is_done,
        )


class TasksModel(BaseModel):
    pk: Optional[int] = None
    title: Optional[str] = None
    description: Optional[str] = None
    media_url: Optional[str] = None
    is_done: Optional[bool] = None
