from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Inisialisasi database
db = SQLAlchemy(app)

from app import routes, models  # Impor rute dan model
