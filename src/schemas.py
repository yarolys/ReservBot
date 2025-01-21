import enum
from datetime import datetime, time, date

from pydantic import BaseModel, HttpUrl, ConfigDict


class KbButtonSchema(BaseModel):
    id: int
    name: str
    url: HttpUrl


class UserSchema(BaseModel):
    id: int
    full_name: str
    created_at: datetime


class WelcomeMessageSchema(BaseModel):
    id: int
    text: str


class SettingsSchema(BaseModel):
    id: int
    welcome_message: str


class ScheduleSchema(BaseModel):
    id: int
    user_id: int
    date: date
    time: time

