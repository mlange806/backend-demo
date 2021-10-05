# Backend Demo
## Building docker image
```bash
docker build -t demo .
```

## Running API
```bash
docker run -d -p 80:80 demo
```

For local testing, API can be reached at http://127.0.0.1:8000 and the docs are
at http://127.0.0.1:8000/docs
