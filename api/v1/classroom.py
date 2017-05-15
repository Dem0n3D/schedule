# -*- coding: utf_8 -*-

from flask.ext.restful.reqparse import RequestParser
from flask_restful import Resource
from flask import request

from alchemy import db
from models.classroom import Classroom
from .api_v1 import api_v1


parser = RequestParser()
parser.add_argument("number", type=str, required=True)


class ClassRoomResource(Resource):

    def get(self, id):
        cr = db.session.query(Classroom).get(id)
        return {
            "id": id,
            "number": cr.number,
        }

    def delete(self, id):
        cr = db.session.query(Classroom).get(id)
        db.session.delete(cr)
        db.session.commit()

        return {}, 204

    def put(self, id):
        cr = db.session.query(Classroom).get(id)

        args = parser.parse_args()

        for k, v in args.items():
            setattr(cr, k, v)

        db.session.commit()

        return {
            "id": id,
            "number": cr.number,
        }, 201

class ClassRoomListResource(Resource):

    def get(self):
        classes = db.session.query(Classroom).all()
        return [{
            "id": cr.id,
            "number": cr.number,
        } for cr in classes]

    def post(self):
        args = parser.parse_args()

        cr = Classroom(**args)
        db.session.add(cr)
        db.session.commit()

        return {
            "id": cr.id,
            "number": cr.number,
        }, 201

api_v1.add_resource(ClassRoomListResource, "/classroom")
api_v1.add_resource(ClassRoomResource, "/classroom/<int:id>")
