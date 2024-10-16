# run.py
from app import app
from config import Config

# Menggunakan konfigurasi dari config.py
app.config.from_object(Config)

if __name__ == '__main__':
    app.run()
