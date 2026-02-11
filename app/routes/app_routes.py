from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

# =========================
# ROUTES
# =========================

@main_bp.route("/")
def index():
    return render_template("pages/index.html")


# =========================
# ERROR HANDLER
# =========================

# rate limit
@main_bp.app_errorhandler(429)
def ratelimit_handler(e):
    return render_template("errors/429.html"), 429

# forbidden
@main_bp.app_errorhandler(405)
def ratelimit_handler(e):
    return "Methode Not Allowed", 405