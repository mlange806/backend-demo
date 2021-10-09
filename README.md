# Backend Demo
You will need a local mysql database to connect to. Once that is running, you can configure your own environment variables with a `.env` file. Example:
```
DB_USER='root'
DB_PASS=''
DB_HOST='localhost'
DB_PORT='3306'
DB_NAME='Netflix'
JWT_SECRET='jwtsecret'
API_USERNAME='admin'
# This is 'secret' hashed
API_PASSWORD='$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW'
DB_SOCKET_DIR='/var/run/mysqld'
CLOUD_SQL_CONNECTION_NAME='mysqld.sock'
```

I recommend using a python virtual environment:
```bash
$ python -m venv venv
$ source venv/bin/activate
```

Install requirements.txt and the package:
```bash
(venv) $ pip install -r requirements.txt
(venv) $ pip install .
```

You can run the tests locally with tox:
```bash
(venv) $ pip install tox
(venv) $ tox
```

Now run the API:
```bash
(venv) $ uvicorn app.main:app --reload
```

You can view the docs at http://localhost:8000/docs
