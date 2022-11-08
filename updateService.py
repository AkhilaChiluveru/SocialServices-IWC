# This is a helper file in update process. This file uniquelt identifies what row is needed to update. Capture that row from database and sends to updateSevice.html file.
from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel

class updateService(MethodView):
    def get(self,id):
        model = gbmodel.get_model()
        services=model.selectById(id)
        return render_template('updateService.html',services=services)

    def post(self,id):
        """
        Accepts POST requests, and updates the form into database;
        Redirect to allServices when completed.
        """
        model = gbmodel.get_model()
        model.update(id,request.form['name_of_service_organization'], request.form['type_of_service'], request.form['location'],request.form['phone_number'],request.form['operating_hours'],request.form['review'])
        return redirect(url_for('allServices'))