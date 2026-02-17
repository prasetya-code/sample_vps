from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix

def create_app():
    # initialze core
    core = Flask(__name__, static_folder='static', template_folder='templates')

    # 1️⃣ Terapkan ProxyFix untuk Traefik
    core.wsgi_app = ProxyFix(
        core.wsgi_app,
        x_for=1,     # IP client asli
        x_proto=1,   # scheme (http/https)
        x_host=1     # host
    )
    
    # register config
    from config import register_config
    register_config(core)

    # register routes
    from app.routes import register_routes
    register_routes(core)

    return core