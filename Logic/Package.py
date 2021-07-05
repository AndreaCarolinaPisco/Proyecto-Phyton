from Logic.Person import Person


class Package (object):
    """
    Class used to represent a Package
    """

    def __init__(self, code: str = "0000000", weight: float = 0.0,
                 cost: float = 0.0, description: str = "Paquete", sender: Person= None,
                 receiver: Person= None):
        """ Package constructor object.
        :param code: code of the package.
        :type code: str
        :param weight: weight of the package.
        :type weight: float
        :param cost: cost per gram.
        :type cost: float
        :param description: description of the package.
        :type description: str
        :param sender: person who sends the package.
        :type sender: Person
        :param receiver: person who receives the package.
        :type receiver: Person
        :returns: Package object
        :rtype: object
        """

        self.__code = code
        self.__weight = weight
        self.__cost = cost
        self.__description = description
        self.__sender = sender
        self.__receiver = receiver

    @property
    def code(self):
        """ Returns the code of the package.
                :returns: code of package.
                :rtype: str
                """
        return self.__code

    @code.setter
    def code(self, code: str):
        """ The code of the package is assigned.
                :param code: code of the package.
                :type: str
                """
        self.__code = code

    @property
    def weight(self):
        """ Returns the weight of the package.
                :returns: weight of package.
                :rtype: float
                """
        return self.__weight

    @weight.setter
    def weight(self, weight: float):
        """ The weight of the package is assigned.
                 :param weight: weight of the package.
                 :type: float
                 """
        self.__weight = weight

    @property
    def cost(self):
        """ Returns the cost of the package.
                        :returns: cost of package.
                        :rtype: str
                        """
        return self.__cost

    @cost.setter
    def cost(self, cost: float):
        """ The cost of the package is assigned.
                         :param cost: cost of the package.
                         :type: float
                         """
        self.__cost = cost

    @property
    def description(self):
        """ Returns the description of the package.
                                :returns: description of package.
                                :rtype: float
                                """
        return self.__description

    @description.setter
    def description(self, description: str):
        """ The description of the package is assigned.
                                 :param description: description of the package.
                                 :type: str
                                 """
        self.__description = description

    @property
    def sender(self):
        """ Returns the sender of the package.
                                        :returns: sender of package.
                                        :rtype: str
                                        """
        return self.__sender

    @sender.setter
    def sender(self, sender: Person):
        """ The sender of the package is assigned.
                                         :param sender: sender of the package.
                                         :type: str
                                         """
        self.__sender = sender

    @property
    def receiver(self):
        """ Returns the receiver of the package.
                                                :returns: receiver of package.
                                                :rtype: str
                                                """
        return self.__receiver

    @receiver.setter
    def receiver(self, receiver: Person):
        """ The receiver of the package is assigned.
                                                 :param receiver: receiver of the package.
                                                 :type: str
                                                 """
        self.__receiver = receiver

    def calculate(self):
        return round(self.__weight * self.__cost,1)

    def __str__(self):
        Type = type(self).__name__
        total_cost = str(self.calculate())
        return '[Type - {0}]\n{1}\ncode: {2}\nweight: {3}\ncost: {4}' \
               '\ndescription: {5}\nsender: {6}\nreceiver: {7}\ntotal_cost: {8}'.format(type, 30 * "-", self.code, self.weight,
                                                   self.cost, self.description, self.sender,
                                                   self.receiver, total_cost)


if __name__ == '__main__':
    from Logic.Person import Person

    recep1 = Person(name="Carlos", last_name="Moreno", city="Bogotá")
    remit1 = Person(name="Camilo", last_name="Almeciga", city="Medellin")
    package = Package(code="0234456", weight=2200, cost=50,
                   description="Mercado", sender=remit1, receiver=recep1)
    print(package)

