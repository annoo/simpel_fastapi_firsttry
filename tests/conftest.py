import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import sessionmaker

# from bsdc.account import AccountManager
from bsdc.main import app_maker
# from bsdc.db import get_engine, get_session
# from bsdc.db.models import Base


@pytest.fixture(scope="function")
def session():
    engine = get_engine()
    session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = session_local()
    Base.metadata.bind = engine
    Base.metadata.drop_all()

    try:
        Base.metadata.create_all()
        yield db
    finally:
        db.rollback()


@pytest.fixture
def app(session):
    app = app_maker(testing=True)
    app.dependency_overrides[get_session] = lambda: session
    return app
