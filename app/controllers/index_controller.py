from app.controllers.controller import ControllerBase
from flask import render_template

class IndexController(ControllerBase):
    @staticmethod
    def get():
        body=""""""
        return render_template('index.html')
    @staticmethod
    def getvi():
        return render_template('vi.html')
    @staticmethod
    def getdocker():
        return render_template('docker.html')
    @staticmethod
    def getterm():
        return render_template('terminal.html')

