from abc import ABC
from typing import Any, Optional, Sequence

from sqlalchemy import Engine, Select, select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import DeclarativeMeta, Session


class BaseService(ABC):
    """
    Base service class for interacting with a database table.
    """

    engine: Engine
    model: DeclarativeMeta

    def __init__(self, engine: Engine, model: DeclarativeMeta) -> None:
        """
        Initialize the BaseService class.

        Args:
            engine (Engine): The engine object.
            model (Any): The model object.

        Returns:
            None
        """
        self.engine = engine
        self.model = model

    def find_all(self) -> Sequence:
        """
        Finds all instances of a given instance type.

        Returns:
            A sequence of instances.
        """
        values: Sequence
        try:
            with Session(self.engine) as session:
                statement: Select = select(self.model)
                values = session.execute(statement).scalars().all()
            return values
        except SQLAlchemyError as e:
            print(f"An error occurred while trying to find the instances: {e}")
            return []

    def upsert(self, **kwargs) -> Optional[Any]:
        """
        Upserts a record in the database.

        Args:
            **kwargs: Keyword arguments representing the fields and values of the record.

        Returns:
            Optional[Any]: The upserted record.

        """
        try:
            with Session(self.engine) as session:
                instance = self.find_one(**kwargs)
                if instance:
                    print("...... Doing upsert")
                    for key, value in kwargs.items():
                        if key not in ["email", "uuid"]:
                            setattr(instance, key, value)
                else:
                    instance = self.model(**kwargs)
                    session.add(instance)
                session.commit()
            return instance

        except SQLAlchemyError as e:
            print(f"An error occurred while trying to upsert the instance: {e}")
            return None

    def find_one(self, **kwargs) -> Optional[object]:
        """
        Finds a single instance based on the given criteria.

        Args:
            kwargs: The criteria to filter the instance.

        Returns:
            The matching instance or None if not found.
        """
        try:

            with Session(self.engine) as session:
                statement: Select = select(self.model).filter_by(**kwargs)
                result = session.execute(statement).scalars().first()

            return result

        except SQLAlchemyError as e:
            print(f"An error occurred while trying to find one instance: {e}")
            return None

    def delete(self, **kwargs) -> bool:
        """
        Deletes a single instance based on the given criteria.

        Args:
            kwargs: The criteria to filter the instance.

        Returns:
            True if the instance was deleted, False otherwise.
        """
        try:

            with Session(self.engine) as session:
                instance = self.find_one(**kwargs)

                if instance:
                    session.delete(instance)
                    session.commit()
                    return True

        except SQLAlchemyError as e:
            print(f"An error occurred while trying to delete the instance: {e}")
        return False
