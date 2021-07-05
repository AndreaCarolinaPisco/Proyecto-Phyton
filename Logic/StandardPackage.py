from Logic.Package import Package
from Logic.Person import Person


class StandardPackage(Package):
    """
    Class used to represent a Standard Package
    """

    def __init__(self, code: str = "0000000", weight: float = 0.0,
                 cost: float = 0.1, description: str = "Paquete", sender: Person= None,
                 receiver: Person= None, Fixed_fee: int = 2000):
        """ Standard package constructor object.
             :param fixed_fee: fixed fee for a standard package.
             :type fixed_fee: float
             """
        super().__init__(code, weight, cost, description, sender, receiver)
        self.__Fixed_fee = Fixed_fee

    @property
    def Fixed_fee(self):
        """ Returns the fixed fee for a standard package.
            :returns: fixed fee for a standard package.
            :rtype: float
            """
        return self.__Fixed_fee

    @Fixed_fee.setter
    def Fixed_fee(self, Fixed_fee: int):
        """ Fixed fee for a standard package is assigned.
            :param fixed_fee: fixed fee for a standard package.
            :type: float
            """
        self.__Fixed_fee= Fixed_fee

    def calculate(self):
        return super().calculate()+self.Fixed_fee

    def __str__(self):
        total_Cost= str(self.calculate())
        return super(StandardPackage, self).__str__() + '\n Fixed_fee: {0}'.format(self.Fixed_fee)


if __name__ == '__main__':
    from Logic.Person import Person
    remit2 = Person(name="Marcela", last_name="Moreno", city="Yopal")
    recep2 = Person(name="Hasary", last_name="Malaver", city="Cali")
    standardpackage = StandardPackage(code="0387310738", weight=1800, cost=50,
                description="Libros", sender=remit2, receiver=recep2,Fixed_fee=2000)
    print(standardpackage)
