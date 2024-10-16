import os

class Config:
    SECRET_KEY = 'your_secret_key_here'  # Ganti dengan secret key yang lebih kuat
    DEBUG = True  # Aktifkan debug mode untuk pengembangan

    # Menambahkan konfigurasi database
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
