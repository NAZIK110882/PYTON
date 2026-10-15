"""Тести data_manager: mock, параметризація, перевірка викликів."""
import json
from unittest import mock

import pytest

import data_manager as dm

USERS = [
    {"name": "Олена", "age": 25},
    {"name": "Іван", "age": 17},
    {"name": "Марія", "age": 42},
    {"name": "Петро", "age": 30},
]


# ---------- load_users (mock open) ----------
def test_load_users_uses_mock_open():
    m = mock.mock_open(read_data=json.dumps(USERS))
    with mock.patch("builtins.open", m):
        result = dm.load_users("users.json")
    assert result == USERS
    m.assert_called_once_with("users.json", "r", encoding="utf-8")


def test_load_users_not_a_list():
    m = mock.mock_open(read_data='{"name": "x"}')
    with mock.patch("builtins.open", m):
        with pytest.raises(ValueError):
            dm.load_users("bad.json")


def test_load_users_file_not_found():
    with mock.patch("builtins.open", side_effect=FileNotFoundError):
        with pytest.raises(FileNotFoundError):
            dm.load_users("missing.json")


def test_load_users_invalid_json():
    m = mock.mock_open(read_data="not json")
    with mock.patch("builtins.open", m):
        with pytest.raises(json.JSONDecodeError):
            dm.load_users("broken.json")


# ---------- get_users_older_than (параметризація) ----------
@pytest.mark.parametrize(
    "age, expected_names",
    [
        (0, ["Олена", "Іван", "Марія", "Петро"]),
        (17, ["Олена", "Марія", "Петро"]),
        (25, ["Марія", "Петро"]),
        (41, ["Марія"]),
        (42, []),
        (100, []),
    ],
)
def test_get_users_older_than(age, expected_names):
    result = dm.get_users_older_than(USERS, age)
    assert [u["name"] for u in result] == expected_names


def test_get_users_older_than_empty_list():
    assert dm.get_users_older_than([], 10) == []


def test_get_users_without_age_field():
    assert dm.get_users_older_than([{"name": "Без віку"}], 5) == []


# ---------- load_users_older_than (mock функції) ----------
def test_load_users_older_than_calls_load_users():
    with mock.patch("data_manager.load_users", return_value=USERS) as m_load:
        result = dm.load_users_older_than("users.json", 29)
    m_load.assert_called_once_with("users.json")
    assert [u["name"] for u in result] == ["Марія", "Петро"]


# ---------- save_users (mock open + json.dump) ----------
def test_save_users_writes_file():
    m = mock.mock_open()
    with mock.patch("builtins.open", m), mock.patch("data_manager.json.dump") as m_dump:
        dm.save_users("out.json", USERS)
    m.assert_called_once_with("out.json", "w", encoding="utf-8")
    m_dump.assert_called_once_with(USERS, m(), ensure_ascii=False, indent=4)


def test_save_users_content():
    m = mock.mock_open()
    with mock.patch("builtins.open", m):
        dm.save_users("out.json", USERS)
    written = "".join(c.args[0] for c in m().write.call_args_list)
    assert json.loads(written) == USERS


# ---------- інтеграційний тест з реальним файлом ----------
def test_save_and_load_roundtrip(tmp_path):
    path = tmp_path / "users.json"
    dm.save_users(str(path), USERS)
    assert dm.load_users(str(path)) == USERS
