
DEBUG = True
DIALECT = 'mysql'
DRIVE = 'pymysql'
USERNAME = 'root'
PASSWD = '242501'
HOST = 'localhost'
PORT = '3306'
DATABASE = 'api_test'

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}".format(DIALECT,DRIVE,USERNAME,PASSWD,HOST,PORT,DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = "你好"


