from flask import Flask, send_from_directory
from flask_smorest import Api, Blueprint
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)
api = Api(app)

bp = Blueprint("music", "music", url_prefix="/api", description="Music demo endpoints")

# Endpoint for static stems
@bp.route("/stems/<stem_type>")
def get_stem(stem_type):
    static_folder = os.path.join(app.root_path, "static", "mock")
    stem_map = {
        "guitar": "guitar.mp3",
        "drums": "drums.mp3",
        "vocals": "vocals.mp3",
        "mix": "mix.mp3"
    }
    filename = stem_map.get(stem_type, "guitar.mp3")
    return send_from_directory(static_folder, filename)

api.register_blueprint(bp)

@app.route("/")
def hello():
    return "AlatusAI Music Studio Backend running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
