from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass


class Base(MappedAsDataclass, DeclarativeBase):
    """
    This is the base class for all SQLAlchemy ORM models in the application.

    It inherits from MappedAsDataclass and DeclarativeBase which provide the
    functionality for mapping Python classes to relational database tables.

    All ORM models in the application should inherit from this class to get
    the basic functionality for interacting with the database.
    """

    pass
