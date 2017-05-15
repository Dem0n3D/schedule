# -*- coding: utf_8 -*-

from marshmallow import fields

from models.corpus import Corpus
from .schema import BaseSchema
from .classroom import ClassroomSchema


class CorpusSchema(BaseSchema):
    class Meta(BaseSchema.Meta):
        model = Corpus

    classrooms = fields.List(fields.Nested(ClassroomSchema))
