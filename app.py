from flask import render_template
# import connexion
import config
from models import User

# app = connexion.App(__name__, specification_dir="./")
app = config.connex_app
app.add_api(config.basedir / "swagger.yml")


@app.route("/")
def home():
    user = User.query.all()
    return render_template("home.html", user=user)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
