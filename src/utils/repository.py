from abc import ABC, abstractmethod
from sqlalchemy import Select
from sqlmodel import SQLModel, insert, select
from sqlalchemy.ext.asyncio import AsyncSession


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one(self, session: AsyncSession, data: dict):
        raise NotImplementedError

    @abstractmethod
    async def find_all(self, session: AsyncSession, *filters):
        raise NotImplementedError

    @abstractmethod
    async def find(self, session: AsyncSession, *filters):
        raise NotImplementedError

    @abstractmethod
    async def find_custom(self, session: AsyncSession, statement: Select):
        raise NotImplementedError

    @abstractmethod
    async def update_one(self, session: AsyncSession, data: dict):
        raise NotImplementedError
    
    @abstractmethod
    async def find_all_custom(self, session: AsyncSession, statement: Select):
        raise NotImplementedError
    

class SQLAlchemyRepository(AbstractRepository):
    model = None

    def __init__(self):
        if not self.model:
            raise NotImplementedError("Модель репозитория не найдена")
    
    async def add_one(self, session: AsyncSession, data: dict):
        stmt = insert(self.model).values(**data).returning(self.model)
        result = await session.execute(stmt)
        await session.commit()
        return result.scalar_one_or_none()

    async def find_all(self, session: AsyncSession, offset: int = 0, limit: int = 100, *filters):
        stmt = select(self.model).filter(*filters).offset(offset).limit(limit)
        res = await session.execute(stmt)
        return res.scalars().all()

    async def find(self, session: AsyncSession, *filters):
        stmt = select(self.model).filter(*filters)
        res = await session.execute(stmt)
        return res.scalar_one_or_none()
    
    async def update_one(self, session: AsyncSession, update_dict: dict, schema: SQLModel):
        for key, value in update_dict.items():
            if hasattr(schema, key):
                setattr(schema, key, value)
        
        session.add(schema)
        await session.commit()
        await session.refresh(schema)
        return schema
    
    async def delete_one(self, session: AsyncSession, schema: SQLModel):
        await session.delete(schema)
        await session.commit()
        return True

    async def find_custom(self, session: AsyncSession, statement: Select):
        result = await session.execute(statement)
        return result.scalar_one_or_none()
    
    async def find_all_custom(self, session: AsyncSession, statement: Select):
        result = await session.execute(statement)
        return result.scalars().all()
    
