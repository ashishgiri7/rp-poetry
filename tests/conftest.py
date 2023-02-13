import pytest
from fastapi.testclient import TestClient

from rp_poetry.main import app

# @pytest.fixture(scope="function")
# def app_test():
#     client = TestClient(app)
#     yield client


@pytest.fixture()
def client():
    """Client Fixer for Testing"""
    return TestClient(app)
