import sqlalchemy
from app.config import *
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

metadata_obj = MetaData()
shows_table = Table('SHOWS', metadata_obj,
    Column('show_id', String, primary_key=True),
    Column('type', String),
    Column('title', String),
    Column('director', String),
    Column('cast', String),
    Column('country', String),
    Column('date_added', String),
    Column('release_year', String),
    Column('rating', String),
    Column('duration', String),
    Column('listed_in', String),
    Column('description', String)
)

db = sqlalchemy.create_engine(
    sqlalchemy.engine.url.URL.create(
        drivername="mysql+pymysql",
        username=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        query={
            "unix_socket": "{}/{}".format(
                DB_SOCKET_DIR,
                CLOUD_SQL_CONNECTION_NAME
            )
        }
    )
)


def get_shows():
    with db.connect() as conn:
        stmt = shows_table.select()
        shows = conn.execute(stmt).fetchall()
    return shows


def update_show(show_id, key, value):
    with db.connect() as conn:
        stmt = shows_table.update().\
            where(shows_table.c.show_id == show_id).\
            values({key: value})
        conn.execute(stmt)
