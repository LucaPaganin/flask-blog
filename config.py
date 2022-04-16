import imp
import os
from pathlib import Path

basedir = Path(__file__).absolute().parent

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir/'blog.db'}"
    SQLALCHEMY_TRACK_MODIFICATIONS = True