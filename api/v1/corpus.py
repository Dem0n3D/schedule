# -*- coding: utf_8 -*-

from flask.ext.restful.reqparse import RequestParser
from flask_restful import Resource
from flask import request

from alchemy import db
from models.corpus import Corpus
from schemas.corpus import CorpusSchema
from .api_v1 import api_v1


corpus_schema = CorpusSchema()
corpuss_schema = CorpusSchema(many=True)


class CorpusResource(Resource):

    def get(self, id):
        cr = db.session.query(Corpus).get(id)
        return corpus_schema.dump(cr).data

    def delete(self, id):
        cr = db.session.query(Corpus).get(id)
        db.session.delete(cr)
        db.session.commit()

        return {}, 204

    def put(self, id):
        cr = corpus_schema.load(request.json)
        db.session.commit()
        return corpus_schema.dump(cr.data).data, 201

class CorpusListResource(Resource):

    def get(self):
        classes = db.session.query(Corpus).all()
        return corpuss_schema.dump(classes).data

    def post(self):
        cr = corpus_schema.load(request.json)
        db.session.add(cr.data)
        db.session.commit()
        return corpus_schema.dump(cr.data).data, 201

api_v1.add_resource(CorpusListResource, "/corpus")
api_v1.add_resource(CorpusResource, "/corpus/<int:id>")
