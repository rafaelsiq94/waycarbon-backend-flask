from flask import Flask
from flask_cors import CORS
from config import config
from routes import Carbon

app = Flask(__name__)

CORS(app, resources={"*": {"origins": "http://localhost:3000"}})


def page_not_found(error):
    return "<h1>Página não encontrada</h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])

    # Blueprints
    app.register_blueprint(Carbon.main, url_prefix='/api/carbon')

    # Error handlers
    app.register_error_handler(404, page_not_found)
    app.run()
