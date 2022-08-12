from flask.views import MethodView
from app.models.graphic_options import GraphicOptions

class GraphicsAPI(MethodView):
    def get(GraphicOptions):
        return "Hola"