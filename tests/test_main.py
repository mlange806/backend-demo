import copy
import app.crud as crud
import app.main
import pytest
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
async def test_get_summary():
    crud.get_shows = MagicMock(return_value=DATA)

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

@pytest.mark.asyncio
async def test_get_shows():
    crud.get_shows = MagicMock(return_value=copy.deepcopy(DATA))

    r = await app.main.get_shows(0, 3)
    assert r == DATA[0:3]

    r = await app.main.get_shows(0, 2)
    assert r == DATA[0:2]

    r = await app.main.get_shows(1, 3)
    assert r == DATA[1:3]

    r = await app.main.get_shows(0, 3, search="Dick Johnson Is Dead")
    assert r == DATA[0:1]

    r = await app.main.get_shows(0, 3, search="TV Show")
    assert r == DATA[1:3]

    r = await app.main.get_shows(0, 3, descending=True)
    assert r == DATA[::-1]

    r = await app.main.get_shows(0, 3, filter="Dick Johnson Is Dead")
    assert r == DATA[1:3]

    r = await app.main.get_shows(1, 3, search="September", filter="Ganglands")
    assert r == DATA[1:2]

@pytest.mark.asyncio
async def test_update_show():
    data = copy.deepcopy(DATA)
    def update_show(show_id, key, value):
        for (i, show) in enumerate(data):
            if show['show_id'] == show_id:
                data[i][key] = value

    crud.get_shows = MagicMock(return_value=data)
    crud.update_show = MagicMock(side_effect=update_show)

    r = await app.main.update_show('s1', [("title", "My Really Cool Edit")])
    assert r == None
    assert data[0]['title'] == "My Really Cool Edit"

    show_update = [
        ("director", "Mark"),
        ("country", "Canada")
    ]
    r = await app.main.update_show('s1', show_update)
    assert r == None
    assert data[0]['director'] == "Mark"
    assert data[0]['country'] == "Canada"
