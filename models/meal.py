from datetime import datetime
from flask_login import UserMixin
from sqlalchemy import String, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from database import db


class Meal(db.Model, UserMixin):
    #nome, descricao, data e hora, dentro da dieta ou nao
    id: Mapped[int] = mapped_column(unique=True, nullable=False, primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    description: Mapped[str] = mapped_column(String(80))
    date_time: Mapped[datetime] = mapped_column(nullable=False)
    on_diet: Mapped[bool] = mapped_column(nullable=False)