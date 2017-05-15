from sqlalchemy import *
from sqlalchemy.orm import relationship, backref

from alchemy import db


class Classroom(db.Model):

    id = Column(Integer, primary_key=True)

    number = Column(String(255), nullable=False)

    corpus_id = Column(Integer, ForeignKey("corpus.id"), nullable=False)
    corpus = relationship("Corpus", backref="classrooms")
