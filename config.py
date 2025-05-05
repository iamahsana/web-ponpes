import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'ini-rahasia-ubah-sendiri'
    DATABASE_URI = os.path.join(BASE_DIR, 'erp_pondok.db')
