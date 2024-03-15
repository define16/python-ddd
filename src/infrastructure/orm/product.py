import datetime
from typing import List
from sqlalchemy import Integer, String
from sqlalchemy import ForeignKey, func
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(AsyncAttrs, DeclarativeBase):
    pass


class Option(Base):
    __tablename__ = "product__option"

    id: Mapped[int] = mapped_column(primary_key=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"))
    name: Mapped[str] = mapped_column(String(50), nullable=False)


class Product(Base):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    price: Mapped[int] = mapped_column(Integer())
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())
    options: Mapped[List[Option]] = relationship()
