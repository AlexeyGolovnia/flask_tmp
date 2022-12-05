from flask import Flask
# from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@host.docker.internal:5432/market'
app.config['SECRET_KEY'] = '933a8266efc1bb729e490bdb'
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

from market import routes
