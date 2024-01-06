import web_api
import config
from flask import Flask

app = Flask(__name__)


def check_in():
    app_version = web_api.get_version()
    user_info = web_api.get_user_info()
    combo_token = user_info["combo_token"]
    open_id = user_info["open_id"]
    config.login_headers["X-Rpc-App_version"] = app_version
    config.login_headers["X-Rpc-Combo_token"] = web_api.get_combo_token(combo_token, open_id)
    web_api.login()
    web_api.get_wallet()
    notifications = web_api.get_notifications()
    for notice in notifications:
        web_api.read_notification(notice["id"])


@app.route("/api/check_in", methods=["get"])
def api_check_in():
    check_in()
    return "success"


if __name__ == "__main__":
    app.run(port=14514, debug=True)
