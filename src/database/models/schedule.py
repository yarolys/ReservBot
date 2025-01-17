from sqlalchemy import Date, Time, select, delete
from sqlalchemy.orm import Mapped, mapped_column
from src.database.connection import Base, async_session_maker


class Schedule(Base):
    __tablename__ = 'schedule'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, nullable=False)
    user_id: Mapped[int] = mapped_column(nullable=False)
    date: Mapped[Date] = mapped_column(nullable=False)
    time: Mapped[Time] = mapped_column(nullable=False)


    @classmethod
    async def create_schedule(cls, user_id: int, date: str, time: str):
        from datetime import datetime
        schedule_date = datetime.strptime(date, "%Y-%m-%d").date()
        schedule_time = datetime.strptime(time, "%H:%M").time()

        async with async_session_maker() as session:
            session.add(cls(user_id=user_id, date=schedule_date, time=schedule_time))
            await session.commit()


    @classmethod
    async def get_schedule_by_user(cls, user_id: int) -> list:
        async with async_session_maker() as session:
            schedules = (await session.execute(
                select(cls).where(cls.user_id == user_id)
            )).scalars().all()
            return schedules
        

    @classmethod
    async def get_all_schedules(cls) -> list:
        async with async_session_maker() as session:
            schedules = (await session.execute(select(cls))).scalars().all()
            return schedules
        
    
    @classmethod
    async def delete_schedule(cls, schedule_id: int):
        async with async_session_maker() as session:
            await session.execute(delete(cls).where(cls.id == schedule_id))
            await session.commit()
            