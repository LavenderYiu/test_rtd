""" @package pyexample
Documentation for this module.

More details.
"""
 
def global_func():
    """ Documentation for a function.

    More details.
    """
    pass
 

class PyClass:
    """ Documentation for a class.

    More details.
    """

    static_mem = 0  # A class variable.
   
    def __init__(self):
        """ The constructor.

        More details.
        """
        self.public_mem = 'member'
        self._proteced_mem = 0
        self.__private_mem = True
   
    def public_func(self, param1):
        """ This is a function called public_func.

        :param param1: 1st param
        :return: Boolean. This is a Boolean return.
        """
        return False
    
    def __private_func(self):
        """This is a function called __private_func.
        """
        pass

    @staticmethod
    def static_func(a, b):
        """ This is a function called static_func.

        :param a: param a
        :param b: param b
        """
        pass

    ## @var _memVar
    #  a member variable
