from flask_restx import Resource, Namespace

from dao.model.genre import GenreSchema
from implemented import director_service

genre_ns = Namespace("genre")


@genre_ns.route("/")
class GenreView(Resource):
    def get(self):
        d_objects = director_service.get_all
        result = GenreSchema(many=True).dump(d_objects)
        return result, 200


@genre_ns.route("/<int:uid>")
class GenreView(Resource):
    def get(self, uid):
        g_objects = director_service.get_one(uid)
        result = GenreSchema().dump(g_objects)
        return result, 200
