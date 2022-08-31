from random import randrange

import pytest

from q1_2.class_demo import Felidae, Cat
from q3.lambda_demo import extract_even_integers
from q4.dictionary_demo import find_first_element


class TestSolutions:

    def test_not_implemented_methods(self):
        """
        Test the Felidae class raises a NotImplementedError exception
        :return:
        """
        felidae = Felidae('Leo', 'Leopard', 'black')

        with pytest.raises(NotImplementedError):
            felidae.get_info()
            Felidae.from_string('This is a just a string')

    def test_cat_class(self):
        """
        Test the Cat class behavior
        :return:
        """
        cat = Cat('Mochi', 'red and black', 'salmon', 'ball')
        assert cat.get_info() == "This Felidae is a cat named Mochi. It's fur is red and black. " \
                                 "Want to win it's heart? " \
                                 "Bring some salmon and a new ball."

        cat_from_string = Cat.from_string('Illumi,red and black,tuna,feather')
        assert cat_from_string.get_info() == "This Felidae is a cat named Illumi. It's fur is red and black. " \
                                 "Want to win it's heart? " \
                                 "Bring some tuna and a new feather."

    def test_extract_even_integers(self):
        """
        Test even integers retrieval return the correct list
        :return:
        """
        # This will create a list with exactly 25 even integers
        list_with_integers = list(range(0, 50))
        even_integers = extract_even_integers(list_with_integers)

        for i in even_integers:
            assert i % 2 == 0
        assert len(even_integers) == 25

    def test_extract_even_integers_empty_list(self):
        """
        Test even integers retrieval return an empty list when no even integers are present
        :return:
        """
        # This will create a list without even integers
        list_wo_integers = list(range(1, 10, 2))
        even_integers = extract_even_integers(list_wo_integers)
        assert even_integers == []

        # This will create a bigger list without even integers
        bigger_list_wo_integers = [randrange(1, 10, 2) for i in range(0, 100)]
        bigger_even_integers = extract_even_integers(bigger_list_wo_integers)
        assert bigger_even_integers == []

    def test_find_first_element(self):
        """
        Test the find_first_element function
        :return:
        """
        # This will create a random list of dictionaries with x and y attrs
        dictionaries = [{'x': i, 'y': i} for i in range(0, 10)]
        first_element = find_first_element(dictionaries)

        # dict should not be empty and both x and y attrs should be equal to 5
        assert first_element != {}
        assert first_element['x'] == 5
        assert first_element['y'] == 5

        # This will create a random list of dictionaries with x and y attrs where x = i and y = i*2
        new_dictionaries = [{'x': i, 'y': i*2} for i in range(0, 10)]
        new_first_element = find_first_element(new_dictionaries)

        # dict should not be empty, x attr should be equal to 5 and y attr should be equal to 10
        assert new_first_element != {}
        assert new_first_element['x'] == 5
        assert new_first_element['y'] == 10

    def test_find_first_element_empty_dict(self):
        """
        Test find_first_element returns an empty dict when no dict with x = 5 is found
        :return:
        """
        # This will create a random list of dictionaries with x and y attrs, these attrs will never be equal to 5
        dictionaries = [{'x': i*2, 'y': i*2} for i in range(0, 10)]
        first_element = find_first_element(dictionaries)

        # dict should be empty
        assert first_element == {}