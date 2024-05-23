from sqlalchemy import ForeignKey
from sqlalchemy import String, DateTime, Integer
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass


class Proxy(Base):
    __tablename__ = "proxies"
    id: Mapped[int] = mapped_column(primary_key=True)
    address: Mapped[str] = mapped_column(String(64))

    def __repr__(self) -> str:
        return f"Proxy(id={self.id!r}, address={self.address!r})"


class AuthSession(Base):
    __tablename__ = "auth_sessions"
    id: Mapped[int] = mapped_column(primary_key=True)
    proxy_id: Mapped[int] = mapped_column(ForeignKey("proxies.id"), nullable=True)
    session_id: Mapped[str] = mapped_column(String(32))
    cookie: Mapped[int] = mapped_column(String(32))
    last_usage: Mapped[str] = mapped_column(String(32), nullable=True)
    is_disabled: Mapped[int] = mapped_column(Integer(), default=0)

    proxy = relationship(
        "Proxy"
    )

    def __repr__(self) -> str:
        return f"AuthSession(id={self.id!r}, session_id={self.session_id!r}, cookie={self.cookie!r}, last_usage={self.last_usage!r}, is_disabled={self.is_disabled!r})"
