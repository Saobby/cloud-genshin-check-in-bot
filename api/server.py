import web_api
import config
from flask import Flask

app = Flask(__name__)


def check_in():
    info = web_api.get_user_info()
    combo_token = info["combo_token"]
    open_id = info["open_id"]
    config.login_headers["X-Rpc-Combo_token"] = web_api.get_combo_token(combo_token, open_id)
    web_api.login()


@app.route("/api/check_in", methods=["get"])
def api_check_in():
    check_in()
    return "success"


if __name__ == "__main__":
    app.run(port=14514, debug=True)
