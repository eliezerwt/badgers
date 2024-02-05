from flask import Flask

from model.user import User
from service.database_service import DatabaseService
from service.user_service import UserService
from util.config import config

database_service = DatabaseService(database_url=config.DATABASE_URL)
app: Flask = Flask(__name__)

user_service = UserService(database_service.get_engine())


@app.route("/", methods=["GET"])
def index():
    user_service.upsert(**{"username": "test-test", "email": "email@test.com"})
    return list(user_service.find_all())


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
