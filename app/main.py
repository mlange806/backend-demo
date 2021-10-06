import os
import sqlalchemy
from fastapi import FastAPI

app = FastAPI()

db = sqlalchemy.create_engine(
    sqlalchemy.engine.url.URL.create(
        drivername="mysql+pymysql",
        username=os.environ["DB_USER"],
        password=os.environ["DB_PASS"],
        host=os.environ["DB_HOST"],
        port=os.environ["DB_PORT"],
        database=os.environ["DB_NAME"],
        query={
            "unix_socket": "{}/{}".format(
                os.environ.get("DB_SOCKET_DIR", "/cloudsql"),
                os.environ["CLOUD_SQL_CONNECTION_NAME"]
            )
        }
    )
)


@app.get("/")
async def root():
    shows = []
    with db.connect() as conn:
        shows = conn.execute("SELECT * FROM SHOWS").fetchall()
    return shows
