# this python file calls allServicesList.html file and this is invoked in app.py file and filnally all services page is seen through this
from flask import redirect, request, url_for, render_template
from flask.views import MethodView
from datetime import datetime
import gbmodel

class allServicesList(MethodView):
    def get(self):
        model = gbmodel.get_model()
        services = [dict(id=row[0],name_of_service_organization=row[1], type_of_service=row[2], location=row[3], phone_number=row[4], operating_hours=row[5], review=row[6]) for row in model.select()]
        return render_template('allServicesList.html',services=services)
 
