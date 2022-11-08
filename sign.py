# This is invoked when insertion route is called. After succesful insertion this redirects to allServices route.
from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel

class Sign(MethodView):
    def get(self):
        return render_template('sign.html')

    def post(self):
        """
        Accepts POST requests, and processes the form;
        Redirect to index when completed.
        """
        model = gbmodel.get_model()
        model.insert(request.form['id'],request.form['name_of_service_organization'], request.form['type_of_service'], request.form['location'],request.form['phone_number'],request.form['operating_hours'],request.form['review'])
        return redirect(url_for('index'))