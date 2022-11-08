# This is update path where actual update to database is made invoking mode.update function. after succesful operation this redirects to allService route.
from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel

class Update(MethodView):
    def post(self):
        """
        Accepts POST requests, and processes the form;
        Redirect to all services when completed.
        """
        model = gbmodel.get_model()
        model.update(request.form.get('update_id'),request.form.get('update_name'), request.form.get('update_location'),request.form.get('update_phone_number'),request.form.get('update_operating_hours'),request.form.get('update_review'))
        return redirect(url_for('allServicesList'))