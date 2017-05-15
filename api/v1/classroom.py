# -*- coding: utf_8 -*-

from flask.ext.restful.reqparse import RequestParser
from flask_restful import Resource
from flask import request

from alchemy import db
from models.classroom import Classroom
from schemas.classroom import ClassroomSchema
from .api_v1 import api_v1


classroom_schema = ClassroomSchema()
classrooms_schema = ClassroomSchema(many=True)


class ClassRoomResource(Resource):

    def get(self, id):
        cr = db.session.query(Classroom).get(id)
        return classroom_schema.dump(cr).data

    def delete(self, id):
        cr = db.session.query(Classroom).get(id)
        db.session.delete(cr)
        db.session.commit()

        return {}, 204

    def put(self, id):
        cr = classroom_schema.load(request.json)
        db.session.commit()
        return classroom_schema.dump(cr.data).data, 201

class ClassRoomListResource(Resource):

    def get(self):
        classes = db.session.query(Classroom).all()
        return classrooms_schema.dump(classes).data

    def post(self):
        cr = classroom_schema.load(request.json)
        db.session.add(cr.data)
        db.session.commit()
        return classroom_schema.dump(cr.data).data, 201

api_v1.add_resource(ClassRoomListResource, "/classroom")
api_v1.add_resource(ClassRoomResource, "/classroom/<int:id>")
