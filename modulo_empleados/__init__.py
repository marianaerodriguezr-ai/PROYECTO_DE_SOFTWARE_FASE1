from .empleados_service import EmpleadoService
from .strategies import *

from flask import Flask

def crear_app():
    app = Flask(__name__)
    @app.route('/')
    def home():
        return 'PROYECTO DE SOFTWARE – FASE 1 funcionando'
    return app