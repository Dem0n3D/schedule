from sqlalchemy import *
from sqlalchemy.orm import relationship, backref

from alchemy import db


class Group(db.Model):

    id = Column(Integer, primary_key=True)

    code = Column(String(255), nullable=False)
