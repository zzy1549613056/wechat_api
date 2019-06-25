from flask import Flask,jsonify,url_for
from flask_restful import Api,Resource,reqparse,inputs,fields,marshal_with
from exts import db
import config
from User import User
import requests,json,re
from wechat import wechat



app = Flask(__name__)
app.config.from_object(config)
#app.config['SERVER_NAME'] = 'wechat.test.com'
db.init_app(app)
api = Api(app)

#app.register_blueprint(wechat, subdomain='wechat')



@app.route('/')
def index():
    return jsonify({"name":"作者","age":14})


@app.route('/aa')
def aa():
    return 'aa'


@app.route('/wechat/')
def wechat():
    return 'wechat'
# with app.app_context():
#     print (url_for('index', _external=True))
# @app.route('/exchange/<src_money>')
# def exchange(src_money):
#     url = "http://op.juhe.cn/onebox/exchange/currency"
#     key = 'd5176afd66beeca2af2a355129241ec3'
#     src = src_money
#     tar = 'CNY'
#     params = {
#         'key': key,
#         'from': src,
#         'to': tar
#     }
#     r = requests.post(url=url,data=params)
#     print (r.text)
#     r_dict = json.loads(r.text)
#     if r_dict['reason'] == '查询成功!':
#         return '1'+r_dict['result'][0]['currencyF_Name']+'兑换'+r_dict['result'][0]['exchange']+'人民币'
#     else:
#         return 'error'

class exChange(Resource):
    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('src', type=str, required=True, help='请输入正确货币简称')
        url = "http://op.juhe.cn/onebox/exchange/currency"
        key = 'd5176afd66beeca2af2a355129241ec3'
        src = parse.parse_args().src
        tar = 'CNY'
        params = {
            'key': key,
            'from': src,
            'to': tar
        }
        r = requests.post(url=url, data=params)
        print(r.text)
        r_dict = json.loads(r.text)
        if r_dict['reason'] == '查询成功!':
            return {
                'src':r_dict['result'][0]['currencyF_Name'],
                'exchange':r_dict['result'][0]['exchange'],
                'to':r_dict['result'][0]['currencyT_Name'],
            }
        else:
            return 'error'




class loginView(Resource):
    resource_fields = {
        "info":fields.Nested({
            "username": fields.String(attribute="name"),
            "age": fields.Integer,
            "gender": fields.Boolean,
            "time": fields.DateTime(attribute="create_time")
        })
    }


    def get(self):
        a = {"name":"zzy","age":14}
        return a

    # @marshal_with(resource_fields)
    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('username',type=str,required=True,help='用户名验证错误')
        parse.add_argument('date_time',type=inputs.date,help='时间错误')
        args = parse.parse_args()
        user = User.query.filter(User.name==args.username).first()
        myuser={'username':'朱正阳','age':34}
        return {"info":myuser}


class weijinSearch(Resource):
    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('text', type=str, required=True, help='长度超限')
        parse.add_argument('mgtype', type=int, help='mgtype??')
        parse.add_argument('ty_wj_type', type=int, help='ty_wj_type??')
        parse.add_argument('mz_wj_type', type=int, help='mz_wj_type??')
        parse.add_argument('xw_wj_type', type=int, help='xw_wj_type??')
        text = parse.parse_args().text
        if len(text)>101 :
            text = ''
        mgtype = parse.parse_args().get('mgtype',1)
        ty_wj_type = parse.parse_args().get('ty_wj_type',1)
        mz_wj_type = parse.parse_args().get('mz_wj_type',1)
        w_wj_type = parse.parse_args().get('w_wj_type', 1)
        url = 'http://www.ju1.cn/index.php/Index/add.html'
        data = {'text':text,'mgtype':mgtype,'ty_wj_type':ty_wj_type,'mz_wj_type':mz_wj_type,'xw_wj_type':w_wj_type}
        r = requests.post(url,data=data)
        l = re.match(r'(.*?)\<\<\<(\d+?)\<\<\<(\d+?)\<\<\<(\d+?)\<\<\<(.*?)\<\<\<(.*?)\<\<\<(\d+)',r.text,flags=re.S)
        print(r.text)
        info_str = re.sub('null','\"null\"',l.group(5))
        info = eval(info_str)
        if info:
            info_list = info
        else:
            info_list = ''
        res = {
            'content':l.group(1),
            'sensitive_count':int(l.group(2)),
            'forbid_count':int(l.group(3)),
            'count':int(l.group(4)),
            'info':info_list,
            'other':'',
            'other_count':int(l.group(7))
        }
        return jsonify(res)

api.add_resource(loginView,'/login',endpoint='login')
api.add_resource(exChange,'/exchange',endpoint='exchange')
api.add_resource(weijinSearch,'/wjsearch',endpoint='wjsearch')





# @app.route('/add_sql')
# def hello_world():
#     addUser1 = User(name='zzy',age=25,gender=True)
#     addUser2 = User(name='lla', age=22, gender=False)
#     db.session.add(addUser1)
#     db.session.add( addUser2)
#     db.session.commit()
#     return 'Hello World!'



# with app.app_context():
#     db.create_all()

if __name__ == '__main__':
   # pass
    app.run(debug=True,host='0.0.0.0',port=5001)
