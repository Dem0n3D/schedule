# -*- coding: utf_8 -*-

from flask.ext.restful.reqparse import RequestParser
from flask_restful import Resource
from flask import request

from alchemy import db
from models.group import Group
from schemas.group import GroupSchema
from .api_v1 import api_v1


group_schema = GroupSchema()
groups_schema = GroupSchema(many=True)


class GroupResource(Resource):

    def get(self, id):
        cr = db.session.query(Group).get(id)
        return group_schema.dump(cr).data

    def delete(self, id):
        cr = db.session.query(Group).get(id)
        db.session.delete(cr)
        db.session.commit()

        return {}, 204

    def put(self, id):
        cr = group_schema.load(request.json)
        db.session.commit()
        return group_schema.dump(cr.data).data, 201

class GroupListResource(Resource):

    def get(self):
        classes = db.session.query(Group).all()
        return groups_schema.dump(classes).data

    def post(self):
        cr = group_schema.load(request.json)
        db.session.add(cr.data)
        db.session.commit()
        return group_schema.dump(cr.data).data, 201

api_v1.add_resource(GroupListResource, "/group")
api_v1.add_resource(GroupResource, "/group/<int:id>")
