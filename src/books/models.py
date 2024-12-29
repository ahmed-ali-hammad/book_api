from sqlmodel import SQLModel, Field, Column

from uuid import uuid4, UUID
import sqlalchemy.dialects.postgresql as pg

from datetime import datetime, date


class Book(SQLModel, table=True):
    __tablename__ = "book"

    id: UUID = Field(
        sa_column=Column(pg.UUID, nullable=False, primary_key=True, default=uuid4)
    )
    title: str
    author: str
    publisher: str
    published_date: date
    page_count: int
    language: str
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    updated_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))

    def __repr__(self):
        return f"Book {self.title}"
