from typing import Any

from sqlalchemy import Engine

from abstract.base_service import BaseService


class UserService(BaseService):
    """
    This class represents a user service.

    Args:
        engine (Engine): The database engine.
        model (Any): The object model.

    Attributes:
        engine (Engine): The database engine.
        model (Any): The object model.
    """

    def __init__(self, engine: Engine, model: Any) -> None:
        super().__init__(engine, model)
