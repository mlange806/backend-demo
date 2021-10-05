from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Edit"}

@app.get("/newfeature")
async def new_feature():
    return {"wow!": "cool2"}
