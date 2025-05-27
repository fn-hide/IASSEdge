import uuid
from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship

from app.schemas.site import SiteBase

if TYPE_CHECKING:
    from app.models.user import User


# Database model, database table inferred from class name
class Site(SiteBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    hashed_password: str
    owner_id: uuid.UUID = Field(
        foreign_key="user.id", nullable=False, ondelete="CASCADE"
    )
    owner: "User" = Relationship(back_populates="sites")
