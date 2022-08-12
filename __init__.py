import logging
import os
from flask import Flask
from app import main
from app.controllers.graphics import GraphicsAPI

# Flask App Initialization
app = Flask(__name__)
app.config.from_object(main.settings[os.environ.get('APPLICATION_ENV', 'default')])

# Logs Initialization
console = logging.getLogger('console')

app.add_url_rule('/graphics', view_func=GraphicsAPI(f"graphic"))

# Flask API Initialization
if __name__ == "__main__":
    app.run(debug=True)