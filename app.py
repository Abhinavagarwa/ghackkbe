from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from config import Config
from models import mongo
from routes import webtoon_bp
from auth import auth_bp, jwt

app = Flask(__name__)
app.config.from_object(Config)

mongo.init_app(app)

jwt.init_app(app)

limiter = Limiter(get_remote_address, app=app, default_limits=["100 per day", "10 per minute"])

app.register_blueprint(webtoon_bp)
app.register_blueprint(auth_bp)

if __name__ == '__main__':
    app.run(debug=True)
