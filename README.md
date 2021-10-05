# Backend Demo
## Setup Environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running Local API
```bash
uvicorn main:app --reload
```

The local API can be reached at http://127.0.0.1:8000 and the docs are at
http://127.0.0.1:8000/docs
