from sqlmodel import Session, create_engine, select

from app import crud
from app.core.config import settings
from app.models import Hub, User
from app.repositories import RHub
from app.schemas import HubCreate, UserCreate
from app.services import SHub

engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))


# make sure all SQLModel models are imported (app.models) before initializing DB
# otherwise, SQLModel might fail to initialize relationships properly
# for more details: https://github.com/fastapi/full-stack-fastapi-template/issues/28


def init_db(session: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables uncommenting the next lines
    # from sqlmodel import SQLModel

    # This works because the models are already imported and registered from app.models
    # SQLModel.metadata.create_all(engine)

    user = session.exec(
        select(User).where(User.email == settings.FIRST_SUPERUSER)
    ).first()
    if not user:
        user_in = UserCreate(
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
        )
        user = crud.create_user(session=session, user_create=user_in)

    hub = session.exec(select(Hub).where(Hub.name == settings.DEFAULT_HUB_NAME)).first()
    if not hub:
        hub_in = HubCreate(
            name=settings.DEFAULT_HUB_NAME,
            address=settings.DEFAULT_HUB_ADDRESS,
            latitude=settings.DEFAULT_HUB_LATITUDE,
            longitude=settings.DEFAULT_HUB_LONGITUDE,
            url=settings.DEFAULT_HUB_URL,
            ping_hub_interval=settings.DEFAULT_HUB_PING_INTERVAL,
        )
        repository = RHub(session)
        service = SHub(repository)
        service.create_hub(hub_in=hub_in, user_id=user.id)
