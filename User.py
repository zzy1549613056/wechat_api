from exts import db
from datetime import datetime

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(60),nullable=False)
    age = db.Column(db.Integer,nullable=False)
    gender = db.Column(db.Boolean,nullable=False)
    create_time = db.Column(db.DateTime,default=datetime.now)