class Person(object):

    """
    Class used to represent a Person
    """

    def __init__(self, name: str = 'Name', last_name: str = "LastName", city: str = "City", address: str = "Calle 6"):
        """ Person constructor object.
        :param name: name of the person.
        :type name: str
        :param last_name: last name of the person.
        :type last_name: str
        :param city: city where theperson is sending or receiving the package.
        :type city: str
        :param address: address of the person who is sending or receiving the package.
        :type address: str
        :returns: Person object
        :rtype: object
        """

        self.name = name
        self.last_name = last_name
        self.city = city
        self.address = address

    @property
    def name(self):
        """ Returns the name of the Person.
        :returns: name of Person.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """ The name of the Person is assigned.
         :param name: name of the Person.
         :type: str
         """
        self._name = name

    @property
    def last_name(self):
        """ Returns the last_name of the Person.
         :returns: last_name of Person.
         :rtype: str
         """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        """ The last_name of the Person is assigned.
        :param last_name: last_name of the Person.
        :type: str
        """
        self._last_name = last_name

    @property
    def city(self):
        """ Returns the city of the Person.
        :returns: city of Person.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city: str):
        """ The city of the Person is assigned.
         :param city: city of the Person.
         :rtype: str
         """
        self._city = city

    @property
    def address(self):
        """ Returns the address of the Person.
        :returns: address of Person.
        :rtype: str
        """
        return self._city

    @address.setter
    def address(self, address: str):
        """ The address of the Person is assigned.
         :param address: address of the Person.
         :type: str
         """
        self._address = address

    def __str__(self):
        return '{1}, {0}\n{2}'.format(self._name, self._last_name, self._city)


if __name__ == '__main__':
    client = Person(name="Carlos", last_name="Moreno",city="Bogotá", address="Carrera 17a #2-15")

    print(client)
