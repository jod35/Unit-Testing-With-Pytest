from app import hello,create_account


def test_hello():
    assert hello("JOnathan") == "Hello JOnathan"


def test_create_account():
    assert create_account("Jonathan",12) == "Created user Jonathan"

