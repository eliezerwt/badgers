from os import getenv
from typing import Optional


class Config:
    """
    Defines the required environment variables for the application

    """

    DATABASE_URL: Optional[str]

    def __init__(self) -> None:
        """
        Loads the environment variables at reading time

        """
        self.DATABASE_URL = getenv("DATABASE_URL")


config = Config()
