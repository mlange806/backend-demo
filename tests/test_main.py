import app.crud as crud
import app.main
import pytest
from helpers import MockDb
from unittest.mock import MagicMock

DATA = [
    {
        "show_id": "s1",
        "type": "Movie",
        "title": "Dick Johnson Is Dead",
        "director": "Kirsten Johnson",
        "cast": "",
        "country": "United States",
        "date_added": "September 25, 2021",
        "release_year": "2020",
        "rating": "PG-13",
        "duration": "90 min",
        "listed_in": "Documentaries",
        "description": "As her father nears the end of his life..."
    },
    {
        "show_id": "s2",
        "type": "TV Show",
        "title": "Blood & Water",
        "director": "",
        "cast": "Ama Qamata, Khosi Ngema, Gail Mabalane, Thabang Molaba",
        "country": "South Africa",
        "date_added": "September 24, 2021",
        "release_year": "2021",
        "rating": "TV-MA",
        "duration": "2 Seasons",
        "listed_in": "International TV Shows, TV Dramas, TV Mysteries",
        "description": "After crossing paths at a party, a Cape Town..."
    },
    {
        "show_id": "s3",
        "type": "TV Show",
        "title": "Ganglands",
        "director": "Julien Leclercq",
        "cast": "Sami Bouajila, Tracy Gotoas, Samuel Jouy, Nabiha Akkari",
        "country": "",
        "date_added": "September 24, 2021",
        "release_year": "2021",
        "rating": "TV-MA",
        "duration": "1 Season",
        "listed_in": "Crime TV Shows, International TV Shows",
        "description": "To protect his family from a powerful..."
    }
]

@pytest.mark.asyncio
async def test_root():
    crud.db = MockDb(DATA)

    r = await app.main.get_summary()
    assert r == {
        "total": 3,
        "movie_count": 1,
        "tv_count": 2,
        "most_active_year": 2021,
        "countries": ["South Africa", "United States"],
        "categories": [
            "Crime TV Shows",
            "Documentaries",
            "International TV Shows",
            "TV Dramas",
            "TV Mysteries"
        ]
    }
