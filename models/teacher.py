from sqlalchemy import *
from sqlalchemy.orm import relationship, backref

from alchemy import db


class Teacher(db.Model):

    id = Column(Integer, primary_key=True)

    name = Column(String(255), nullable=False)
