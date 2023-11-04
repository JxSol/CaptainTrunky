from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


class SessionManager:
    """Class that provides sessions for the project."""

    def __init__(self, db_dsn: str, echo: bool = False):
        self.engine = create_engine(
            url=db_dsn,
            echo=echo,
        )

        self.session_factory = sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    def get_session(self) -> Session:
        with self.session_factory() as session:
            return session
