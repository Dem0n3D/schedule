# -*- coding: utf_8 -*-

from models.classroom import Classroom
from .schema import BaseSchema


class ClassroomSchema(BaseSchema):
    class Meta(BaseSchema.Meta):
        model = Classroom
