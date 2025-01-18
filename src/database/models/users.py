from sqlalchemy import BigInteger, String, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from src.database.base import Base
from pydantic import BaseModel
from datetime import datetime
from sqlalchemy import func
from typing import Optional


class User(Base):
    username: Mapped[str] = mapped_column(String(length=1024), nullable=True)
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False)
    user_id: Mapped[int] = mapped_column(BigInteger, default=0)
    started_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    def to_read_model(self):
        return UserModel(
            pk=self.pk,
            username=self.username,
            is_admin=self.is_admin,
            started_at=self.started_at,
            users_id=self.user_id,
        )


class UserModel(BaseModel):
    pk: Optional[int] = None
    username: Optional[str] = None
    is_admin: Optional[bool] = None
    users_id: Optional[int] = None
    started_at: Optional[datetime] = None
