from flask.views import MethodView
from flask import request
from bokeh.plotting import figure, show
from bokeh.embed import json_item
import json

class GraphicsAPI(MethodView):
    def get(self):
        return "Hola"

    def post(selt):
        graphicOptions = request.json
        x = graphicOptions["x"]
        y = graphicOptions["y"]
        title = graphicOptions["title"]
        legend_label = graphicOptions["legendLabel"]
        line_width = graphicOptions["lineWidth"]

        graphic = figure(title = title, x_axis_label = x["label"], y_axis_label = y["label"])

        graphic.line(x["values"], y["values"], legend_label = legend_label, line_width = line_width)

        return json.dumps(json_item(graphic))