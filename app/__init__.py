from flask import Flask
from app.acces_code.adapters.acces_code_controller\
    import acces_blue_print as acces_code


def create_app():
    app = Flask(__name__)
    app.register_blueprint(acces_code)
    app.url_map.strict_slashes = False
    return app

   
