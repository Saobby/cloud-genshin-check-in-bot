import requests
import json
import hashlib
import hmac
import brotli
import config


def hmacsha256(message: str, key: str):
    return hmac.new(key.encode("utf-8"), message.encode("utf-8"), digestmod=hashlib.sha256).hexdigest()


def get_user_info():
    data = {"app_id": config.app_id, "channel_id": config.channel_id}
    rep = requests.post(config.weblogin_url, data=json.dumps(data), headers=config.weblogin_headers)
    rep = json.loads(rep.text)
    if rep["retcode"] != 0:
        raise RuntimeError("webLogin API返回了一个错误: {}".format(rep["message"]))
    return {"combo_token": rep["data"]["combo_token"], "open_id": rep["data"]["open_id"]}


def get_combo_token(combo_token, open_id):
    sign = hmacsha256("app_id={}&channel_id={}&combo_token={}&open_id={}"
                      .format(config.app_id, config.channel_id, combo_token, open_id), config.app_key)
    return "ai={};ci={};oi={};ct={};si={};bi={}".format(config.app_id, config.channel_id, open_id,
                                                        combo_token, sign, config.game_biz)


def login():
    rep = requests.post(config.login_url, headers=config.login_headers)
    rep = json.loads(rep.text)
    if rep["retcode"] != 0:
        raise RuntimeError("login API返回了一个错误: {}".format(rep["message"]))
    
    
def get_notifications():
    rep = requests.get(config.get_notification_url, headers=config.login_headers)
    rep = json.loads(rep.text)
    if rep["retcode"] != 0:
        raise RuntimeError("listNotifications API返回了一个错误: {}".format(rep["message"]))
    return rep["data"]["list"]


def get_wallet():
    rep = requests.get(config.get_wallet_url, headers=config.login_headers)
    rep = json.loads(rep.text)
    if rep["retcode"] != 0:
        raise RuntimeError("wallet/get API返回了一个错误: {}".format(rep["message"]))
    return rep["data"]


def get_version():
    rep = requests.get(config.get_version_url, headers=config.get_config_headers)
    rep = json.loads(rep.text)
    if rep["retcode"] != 0:
        raise RuntimeError("cloud_config API返回了一个错误: {}".format(rep["message"]))
    return rep["data"]["vals"]["web_update_version"]


def read_notification(nid):
    data = {"id": nid}
    rep = requests.post(config.read_notification_url, data=json.dumps(data), headers=config.login_headers)
    rep = json.loads(rep.text)
    if rep["retcode"] != 0:
        raise RuntimeError("ackNotification API返回了一个错误: {}".format(rep["message"]))


if __name__ == "__main__":
    from pprint import pprint
    app_version = get_version()
    user_info = get_user_info()
    combo_token = user_info["combo_token"]
    open_id = user_info["open_id"]
    config.login_headers["X-Rpc-App_version"] = app_version
    config.login_headers["X-Rpc-Combo_token"] = get_combo_token(combo_token, open_id)
    pprint(config.login_headers)
    login()
    pprint(get_wallet())
    notifications = get_notifications()
    for notice in notifications:
        read_notification(notice["id"])
