from flask.views import MethodView
from flask import request

class GraphicsAPI(MethodView):
    def get(self):
        return "Hola"

    def post(selt):
        return request.json