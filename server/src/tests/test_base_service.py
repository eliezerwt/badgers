import unittest

from sqlalchemy import Integer, String, create_engine
from sqlalchemy.orm import Mapped, mapped_column

from abstract.base_service import BaseService
from model.base import Base


class MockedModelSQL(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    __tablename__ = "mock"


# Create a mock SQLAlchemy engine for testing
mock_engine = create_engine("sqlite:///:memory:", echo=False)
Base.metadata.create_all(mock_engine)

# Create a BaseService instance for testing
base_service = BaseService(mock_engine, MockedModelSQL)  # type: ignore
base_service.upsert(**{"id": 1, "name": "Test"})
base_service.upsert(**{"id": 2, "name": "Another Test"})


class TestBaseService(unittest.TestCase):

    def test_find_all(self):
        result = base_service.find_all()
        assert len(result) == 2

    def test_find_one(self):
        result = base_service.find_one(id=1)
        assert result.__dict__["id"] == 1
        assert result.__dict__["name"] == "Test"


if __name__ == "__main__":
    unittest.main()
