"""
A simple social service flask app.
"""
from crypt import methods
from flask import redirect, request, url_for, render_template
import flask
from flask.views import MethodView
from gbmodel import model_sqlite3
from index import Index
from sign import Sign
from allServiciesList import allServicesList
from deleteService import deleteService
from updateService import updateService
from Update import Update

import gbmodel

app = flask.Flask(__name__)

app.add_url_rule('/',
                 view_func=Index.as_view('index'),
                 methods=["GET"])

app.add_url_rule('/sign/',
                 view_func=Sign.as_view('sign'),
                 methods=['GET', 'POST'])

app.add_url_rule('/allServicesList/',
                 view_func=allServicesList.as_view('allServicesList'),
                 methods=["GET"])

app.add_url_rule('/allServicesList/<id>/deleteService',
                view_func=deleteService.as_view('deleteService'),
                methods=['GET'])

app.add_url_rule('/allServicesList/<id>/updateService',
                view_func=updateService.as_view('updateService'),
                methods=['GET'])
                
app.add_url_rule('/update/',
                view_func=Update.as_view('update'),
                methods=['POST'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
