from flask import Flask
from .extensions import db, migrate
from .routes.filme import filme_bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)


    migrate.init_app(app)

    app.register_blueprint(filme_bp)


    @app.route('/health')
    def health():
        return 'Up and Running', 200

    return app
