import uuid

from app.api.deps import SessionDep
from app.interfaces import ISite
from app.models import Site
from app.repositories import RBase


class RSite(RBase[Site, uuid.UUID], ISite):
    def __init__(self, session: SessionDep) -> None:
        super().__init__(session, Site)
