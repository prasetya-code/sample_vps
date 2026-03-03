from flask import Flask

def create_app():
    # initialze core
    core = Flask(__name__, static_folder='static', template_folder='templates')
    
    # CONFIG
    from config import register_config
    register_config(core)

    # ROUTES
    from app.routes import register_routes
    register_routes(core)

    return core