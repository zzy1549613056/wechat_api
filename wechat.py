from flask import Blueprint


wechat = Blueprint('wechat', __name__)


@wechat.route('/')
def index():
    return '二级域名'