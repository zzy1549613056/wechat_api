from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from flask_resful import app
from exts import db
from User import User

manager = Manager(app)

migrate = Migrate(app,db)

manager.add_command('db',MigrateCommand)

if __name__ == "__main__":
    manager.run()
