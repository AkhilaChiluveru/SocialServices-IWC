# this python file redirects to allServicesList file and this is invoked in app.py file 
from flask import redirect, request, url_for, render_template
from flask.views import MethodView
from datetime import datetime
import gbmodel

class deleteService(MethodView):
   def get(self,id):
      """
      Accepts GET requests, and delet that row from table;
      Redirect to allservice route when completed.
      """
      model = gbmodel.get_model()
      model.delete(id)
      return redirect(url_for('allServicesList'))
        