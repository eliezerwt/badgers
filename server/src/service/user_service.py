from sqlalchemy import Engine

from abstract.user_service import UserService as AbsractUserService
from model.user import User


class UserService(AbsractUserService):
    """
    UserService: is responsible to save, retrieve and delete records from the
    user table in the database using the SQL Alchemy ORM funcionalities.
    """

    engine: Engine

    def __init__(self, engine: Engine) -> None:
        super().__init__(engine, User)
