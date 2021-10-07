import sqlalchemy
from app.config import *

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
        shows = conn.execute("SELECT * FROM SHOWS").fetchall()
    return shows
