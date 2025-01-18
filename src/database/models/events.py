from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Text
from src.database.base import Base
from pydantic import BaseModel
from typing import Optional


class Event(Base):
    title: Mapped[str] = mapped_column(String(length=1024))
    description: Mapped[str] = mapped_column(Text())
    media_url: Mapped[str] = mapped_column(String(length=1024))

    def to_read_model(self):
        return EventModel(
            pk=self.pk,
            title=self.title,
            description=self.description,
            media_url=self.media_url,
        )


class EventModel(BaseModel):
    pk: Optional[int] = None
    title: Optional[str] = None
    description: Optional[str] = None
    media_url: Optional[str] = None
