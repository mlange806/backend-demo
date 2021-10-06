import app.main
import pytest
from helpers import MockDb
from unittest.mock import MagicMock


@pytest.mark.asyncio
async def test_root():
    app.main.db = MockDb(
        [
            {"foo": "bar", "baz": "qux"},
            {"apple": "banana", "pear": "orange"},
        ]
    )

    r = await app.main.root()
    assert r == [
        {"foo": "bar", "baz": "qux"},
        {"apple": "banana", "pear": "orange"},
    ]
