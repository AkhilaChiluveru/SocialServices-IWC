class Model():
    def select(self):
        """
        Gets all entries from the database
        :return: Tuple containing all rows of database
        """
        pass

    def insert(self,id,name_of_service_organization, type_of_service, location, phone_number, operating_hours,review):
       
        """
        Inserts services into database
        :param id :number
        :param name_of_service_organization: String
        :param type_of_service: String
        :Param location: string
        :Param operating_hours String
        :param phone_number string
        :Param review string
        :return: True
        :raises: Database errors on connection and insertion
        """
        pass

    def update(self,id,name_of_service_organization, type_of_service, location, phone_number, operating_hours,review):
       
        """
        Update service into database
        :param id :number
        :param name_of_service_organization: String
        :param type_of_service: String
        :Param location: string
        :Param operating_hours String
        :param phone_number string
        :Param review string
        :return: True
        :raises: Database errors on connection and insertion
        """
        pass
    def delete(self,id):
        """
        Gets all entries from the database
        :return: Tuple containing all rows of database
        """
        pass