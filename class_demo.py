class Felidae:

    def __init__(self, name, species, color):
        """
        Initialize a Felidae object
        :param name: the name of the animal
        :param species: the species of the animal
        :param color: the color of the animal
        """
        self.name = name
        self.species = species
        self.color = color

    @classmethod
    def from_string(cls, string):
        """
        This method will not be implemented in Felidae class
        :param string:
        :return:
        """
        raise NotImplementedError

    def get_info(self):
        """
        This method will not be implemented in Felidae class
        :return:
        """
        raise NotImplementedError
