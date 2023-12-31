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
        raise RuntimeError("API返回了一个错误: {}".format(rep["message"]))
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
        raise RuntimeError("API返回了一个错误: {}".format(rep["message"]))


if __name__ == "__main__":
    pass
