import uuid
from datetime import datetime

from sqlalchemy import Boolean, DateTime, String
from sqlalchemy.orm import Mapped, mapped_column, registry

from model import base
from model.base import Base

reg = registry()


class User(Base):
    """
    Represents a user in the system.
    """

    __tablename__ = "users"

    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    picture: Mapped[str] = mapped_column(String, nullable=True, default=None)
    is_visible: Mapped[Boolean] = mapped_column(Boolean, default=True)
    is_admin: Mapped[Boolean] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow())

    # Primary Key
    uuid: Mapped[str] = mapped_column(
        String, default=str(uuid.uuid4()), primary_key=True
    )
