import app.crud as crud
from app.security import *
from collections import Counter
from datetime import timedelta
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

app = FastAPI()


@app.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/summary")
async def get_summary(current_user: User = Depends(get_current_active_user)):
    shows = crud.get_shows()
    type_count = Counter(s['type'] for s in shows)
    year_count = Counter(int(s["release_year"]) for s in shows)

    countries = set()
    for show in shows:
        countries |= set(filter(None, show['country'].split(', ')))

    categories = set()
    for show in shows:
        categories |= set(filter(None, show['listed_in'].split(', ')))

    return {
        "total": len(shows),
        "movie_count": type_count["Movie"],
        "tv_count": type_count["TV Show"],
        "most_active_year": max(year_count, key=year_count.get),
        "countries": sorted(list(countries)),
        "categories": sorted(list(categories))
    }
