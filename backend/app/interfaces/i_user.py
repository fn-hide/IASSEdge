import uuid

from app.models import User

from .i_base import IBase


class IUser(IBase[User, uuid.UUID]):
    pass
