import pytest


@pytest.fixture(scope='class')
def open():
    print('【开始计算】来自conftest')
    yield
    print('【计算结束】来自conftest')