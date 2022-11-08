"""
Python list model
"""

from .Model import Model

class model(Model):
    def __init__(self):
        self.socialservices = []

    def select(self):
        """
        Returns  list services of lists
        services contains: id,name, location, Type_Of_Service, Phone_Number, Hours_Of_Operation, reviews
        :return: List of lists
        """
        return self.socialservices

    def insert(self,id,name_of_service_organization, type_of_service, location,  phone_number, operating_hours,review):
        """
        Appends a new list of values representing new message into social service
        :param id : number
        :param name_of_service_organization: String
        :param type_of_service: String
        :Param location: string
        :Param operating_hours datetime
        :param phone_number string
        :Param review string
        :return: True
        """
        params = [id,name_of_service_organization, type_of_service, location,  phone_number,operating_hours, review]
        self.socialservices.append(params)
        return True

    def update(self,id,name_of_service_organization, type_of_service, location,  phone_number, operating_hours,review):
        """
        Updates new values of social service
        :param id : number
        :param name_of_service_organization: String
        :param type_of_service: String
        :Param location: string
        :Param operating_hours datetime
        :param phone_number string
        :Param review string
        :return: True
        """
        params = [id,name_of_service_organization, type_of_service, location,  phone_number,operating_hours, review]
        self.socialservices.append(params)
        return True
        
    def delete(self,id):
        """
        Deletes a social service
        :param id : number
        """
        params = [id]
        self.socialservices.append(params)
        return True    