from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column
db = SQLAlchemy()

class Fact(db.Model):
  __tablename__ = 'facts'

  id: Mapped[int] = mapped_column(primary_key=True)
  submitter: Mapped[str]
  fact: Mapped[str]