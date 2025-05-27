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
    username: str = Field(min_length=1, max_length=255)
    password: str = Field(min_length=8, max_length=40)
    ip: str = Field(min_length=1, max_length=255)
    port: int
    url: str


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
    username: str | None = Field(min_length=1, max_length=255)  # type: ignore
    password: str = Field(min_length=8, max_length=40)  # type: ignore
    ip: str | None = Field(min_length=1, max_length=255)  # type: ignore
    port: int | None  # type: ignore
    url: str | None  # type: ignore


# Properties to return via API, id is always required
class SitePublic(SiteBase):
    id: uuid.UUID
    owner_id: uuid.UUID


class SitesPublic(BaseModel):
    data: list[SitePublic]
    count: int
