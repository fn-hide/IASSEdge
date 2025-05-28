import uuid

from sqlmodel import Field

from app.models.base import BaseModel


# Shared properties
class SiteBase(BaseModel):
    name: str = Field(min_length=1, max_length=255)
    address: str = Field(min_length=1, max_length=255)
    latitude: float
    longitude: float
    model: str = Field(min_length=1, max_length=255)
    url: str
    ping_hub_interval: int = Field(ge=1, le=60 * 60 * 24)


# Properties to receive on item creation
class SiteCreate(SiteBase):
    pass


# Properties to receive on item update
class SiteUpdate(SiteBase):
    name: str | None = Field(default=None, min_length=1, max_length=255)  # type: ignore
    address: str | None = Field(default=None, min_length=1, max_length=255)  # type: ignore
    latitude: float | None  # type: ignore
    longitude: float | None  # type: ignore
    model: float | None  # type: ignore
    url: str | None  # type: ignore
    ping_hub_interval: int | None  # type: ignore


# Properties to return via API, id is always required
class SitePublic(SiteBase):
    id: uuid.UUID
    owner_id: uuid.UUID


class SitesPublic(BaseModel):
    data: list[SitePublic]
    count: int
