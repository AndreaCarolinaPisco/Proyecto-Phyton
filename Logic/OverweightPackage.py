from Logic.Package import Package
from Logic.Person import Person


class OverweightPackage(Package):
    """
    Class used to represent a Overweight Package
    """

    def __init__(self, code: str = "0000000", weight: float =0.0,
                 cost: float = 0.0, description: str = "Paquete", sender: Person= None,
                 receiver: Person= None, cost_overweight : float = 0.0):

        """ Overweight package constructor object.
             :param overweight_cost: additional cost of an overweight package.
             :type overweight_cost: float
        """

        super().__init__(code, weight, cost, description, sender, receiver)
        self.__cost_overweight = cost_overweight


    @property
    def cost_overweight(self):
        """ Returns additional cost of an overweight package.
           :returns: additional cost of an overweight package.
           :rtype: float
           """
        return self.__cost_overweight

    @cost_overweight.setter
    def cost_overweight(self, cost_overweight: float):

        """ Additional cost of an overweight package is assigned.
               :param overweight_cost: additional cost of an overweight package.
               :type: float
               """
        self.__cost_overweight= cost_overweight

    def calculate(self):
        return super().calculate()+self.cost_overweight

    def __str__(self):
        Total_cost= str(self.calculate())
        return super(OverweightPackage, self).__str__() + '\n cost_overweight: {0}'.format(self.cost_overweight)


if __name__ == '__main__':
    from Logic.Person import Person
    remit3 = Person(name="Nicolas", last_name="Montoya", city="Tunja")
    recep3 = Person(name="Sebastian", last_name="Malaver", city="Cucuta")
    overweightpackage = OverweightPackage(code="0387310738", weight=1800.9, cost=50.0,
                description="Libros", sender=remit3, receiver=recep3,cost_overweight=3000.0)
    print(overweightpackage)
