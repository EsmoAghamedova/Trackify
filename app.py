from flask import Flask
from app.routes.user import user_bp
from app.routes.admin import admin_bp
from app.routes.auth import auth_bp
from app.routes.company import company_bp
from app.routes.public import public_bp

app = Flask(__name__, template_folder="app/templates", static_folder="app/static")

app.register_blueprint(user_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(company_bp)
app.register_blueprint(public_bp)

if __name__ == '__main__':
    app.run(debug=True, port=5001)