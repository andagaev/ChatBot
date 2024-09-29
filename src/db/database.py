import os

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

    id: orm.Mapped[str] = orm.mapped_column(sa.String, primary_key=True)
    username: orm.Mapped[str] = orm.mapped_column(sa.String(30))


class DiscordUser(Base):
    __tablename__ = "discord_users"

    id: orm.Mapped[str] = orm.mapped_column(sa.String(36), primary_key=True)
    username: orm.Mapped[str] = orm.mapped_column(sa.String(36))


class DiscordChannel(Base):
    __tablename__ = "discord_channels"

    id: orm.Mapped[str] = orm.mapped_column(sa.String(36), primary_key=True)
    name: orm.Mapped[str] = orm.mapped_column(sa.String(36))


def create_tg_user(user_id: str, username: str) -> bool:
    engine = create_engine()

    Base.metadata.create_all(engine)

    with orm.Session(engine, expire_on_commit=False) as session:

        existing_user = session.query(TGUser).filter_by(id=user_id).first()

        if existing_user:
            return False

        new_user = TGUser(username=username, id=user_id)

        session.add(new_user)
        session.commit()
        session.refresh(new_user)

        return True


def create_discord_user(user_id: str, username: str) -> bool:
    engine = create_engine()

    Base.metadata.create_all(engine)

    with orm.Session(engine, expire_on_commit=False) as session:

        existing_user = session.query(DiscordUser).filter_by(id=user_id).first()

        if existing_user:
            return False

        new_user = DiscordUser(id=user_id, username=username)

        session.add(new_user)
        session.commit()
        session.refresh(new_user)

        return True


def create_discord_channel(channel_id: int, channel_name: str) -> bool:
    engine = create_engine()

    Base.metadata.create_all(engine)

    with orm.Session(engine, expire_on_commit=False) as session:

        existing_channel = (
            session.query(DiscordChannel).filter_by(id=channel_id).first()
        )

        if existing_channel:
            return False

        new_channel = DiscordChannel(id=channel_id, name=channel_name)

        session.add(new_channel)
        session.commit()
        session.refresh(new_channel)

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


def get_discord_channels():
    engine = create_engine()

    with orm.Session(engine, expire_on_commit=False) as session:
        channels = session.query(DiscordChannel).all()

    return channels
