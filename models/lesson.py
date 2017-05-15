from sqlalchemy import *
from sqlalchemy.orm import relationship, backref

from alchemy import db


class Lesson(db.Model):
    __table_args__ = (
        UniqueConstraint("day", "number", "teacher_id"),
        UniqueConstraint("day", "number", "group_id"),
        UniqueConstraint("day", "number", "classroom_id"),
    )

    id = Column(Integer, primary_key=True)

    day = Column(Integer, nullable=False)  # day of week
    number = Column(Integer, nullable=False)  # lesson number (daywise)

    classroom_id = Column(Integer, ForeignKey("classroom.id"), nullable=False)
    classroom = relationship("Classroom", backref="lessons")

    teacher_id = Column(Integer, ForeignKey("teacher.id"), nullable=False)
    teacher = relationship("Teacher", backref="lessons")

    group_id = Column(Integer, ForeignKey("group.id"), nullable=False)
    group = relationship("Group", backref="lessons")
