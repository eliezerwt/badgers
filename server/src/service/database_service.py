from typing import Optional

from sqlalchemy import Engine, create_engine

from model.base import Base


class DatabaseService:
    """
    DatabaseService class manages the state of the database connection and the structure
    following the ORM definitions in the implemented classes

    """

    engine: Engine

    def __init__(self, database_url: Optional[str]) -> None:
        """
        Init a new or an existent database, using as default an sqlite in memory database.

        """
        self.engine = create_engine(database_url or "sqlite://", echo=True)
        Base.metadata.create_all(self.engine, checkfirst=True)

    def get_engine(self) -> Engine:
        """
        Returns the DB Engine

        return: SQLAlchemy DB Engine
        """
        return self.engine
