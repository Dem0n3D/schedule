# -*- coding: utf_8 -*-

from marshmallow import fields

from models.group import Group
from .schema import BaseSchema
from .classroom import ClassroomSchema


class GroupSchema(BaseSchema):
    class Meta(BaseSchema.Meta):
        model = Group
