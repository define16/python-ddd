import pytest

from src.infrastructure.mysql.db_context import DbContext
from src.infrastructure.orm.product import Product, Option


@pytest.mark.asyncio
async def test_db_context():
    db_context = DbContext()
    # 테이블 생성
    # async with db_context.connection.begin() as conn:
    #     await conn.run_sync(Base.metadata.create_all)
    db_context.session.add_all(
        [
            Product(options=[Option(name="a"), Option(name="b")], name="product1", price=100),
            Product(options=[Option(name="c")], name="product1", price=1000),
            Product(options=[Option(name="d"), Option(name="e")], name="product1", price=200),
        ]
    )
    await db_context.session.commit()
    await db_context.session.close()
