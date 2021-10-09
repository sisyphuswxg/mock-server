from flask_migrate import Migrate

from MockServer import app, db


migrate = Migrate(app, db)


