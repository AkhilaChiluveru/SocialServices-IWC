# This is index.py file that acts as home page and main route 
from flask import render_template
from flask.views import MethodView
import gbmodel

class Index(MethodView):
    def get(self):
        model = gbmodel.get_model()
        return render_template('index.html')