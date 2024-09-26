import os
import uuid

import sqlalchemy as sa
from sqlalchemy import orm

db_url = os.environ["DATABASE_URL"]


def create_engine() -> sa.Engine:
    engine = sa.create_engine(url=db_url)
    return engine


class Base(orm.DeclarativeBase):
    pass


class TGUser(Base):
    __tablename__ = "tg_users"

    id: orm.Mapped[str] = orm.mapped_column(
        sa.String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    username: orm.Mapped[str] = orm.mapped_column(sa.String(30))


class DiscordUser(Base):
    __tablename__ = "discord_users"

    id: orm.Mapped[str] = orm.mapped_column(
        sa.String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    username: orm.Mapped[str] = orm.mapped_column(sa.String(30))


def create_tg_user(username: str) -> bool:
    engine = create_engine()

    Base.metadata.create_all(engine)

    with orm.Session(engine, expire_on_commit=False) as session:

        existing_user = session.query(TGUser).filter_by(username=username).first()

        if existing_user:
            return False

        new_user = TGUser(username=username)

        session.add(new_user)
        session.commit()
        session.refresh(new_user)

        return True


def create_discord_user(username: str) -> bool:
    engine = create_engine()

    Base.metadata.create_all(engine)

    with orm.Session(engine, expire_on_commit=False) as session:

        existing_user = session.query(DiscordUser).filter_by(username=username).first()

        if existing_user:
            return False

        new_user = DiscordUser(username=username)

        session.add(new_user)
        session.commit()
        session.refresh(new_user)

        return True


def get_tg_users():
    engine = create_engine()

    with orm.Session(engine, expire_on_commit=False) as session:
        users = session.query(TGUser).all()

    return users


def get_discord_users():
    engine = create_engine()

    with orm.Session(engine, expire_on_commit=False) as session:
        users = session.query(DiscordUser).all()

    return users
