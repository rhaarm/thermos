import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = '\xb0\x0e\x02|\xed\x84\x93\x1de2\x11r\x1f\x02\xb7\xfa*\xd3\xdb\xca\xaa\x90\x06\xce'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'thermos.db')
db = SQLAlchemy(app)

import models
import views