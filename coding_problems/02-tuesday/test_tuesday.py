# pylint: skip-file

import pytest

from tuesday import diamond

example_1 = "*\n"

example_3 = " *\n"
example_3 += "***\n"
example_3 += " *\n"

example_5 = "  *\n"
example_5 += " ***\n"
example_5 += "*****\n"
example_5 += " ***\n"
example_5 += "  *\n"


def test_basic_test_1():
    assert diamond(1) == example_1


def test_basic_test_2():
    assert diamond(2) == None


def test_basic_test_3():
    assert diamond(3) == example_3


def test_basic_test_4():
    assert diamond(5) == example_5


def test_basic_test_5():
    assert diamond(0) == None


def test_basic_test_6():
    assert diamond(-3) == None


@pytest.mark.parametrize("a,b",
                         [(12, None),
                          (5, '  *\n ***\n*****\n ***\n  *\n'),
                             (3, ' *\n***\n *\n'),
                             (-17, None),
                             (16, None),
                             (12, None),
                             (15, '       *\n      ***\n     *****\n    *******\n   *********\n  ***********\n *************\n***************\n *************\n  ***********\n   *********\n    *******\n     *****\n      ***\n       *\n'),
                             (6, None),
                             (-2, None),
                             (-7, None),
                             (0, None),
                             (14, None),
                             (15, '       *\n      ***\n     *****\n    *******\n   *********\n  ***********\n *************\n***************\n *************\n  ***********\n   *********\n    *******\n     *****\n      ***\n       *\n'),
                             (1, '*\n'),
                             (19, '         *\n        ***\n       *****\n      *******\n     *********\n    ***********\n   *************\n  ***************\n *****************\n*******************\n *****************\n  ***************\n   *************\n    ***********\n     *********\n      *******\n       *****\n        ***\n         *\n'),
                             (17, '        *\n       ***\n      *****\n     *******\n    *********\n   ***********\n  *************\n ***************\n*****************\n ***************\n  *************\n   ***********\n    *********\n     *******\n      *****\n       ***\n        *\n'),
                             (7, '   *\n  ***\n *****\n*******\n *****\n  ***\n   *\n'),
                             (6, None),
                             (9, '    *\n   ***\n  *****\n *******\n*********\n *******\n  *****\n   ***\n    *\n'),
                             (9, '    *\n   ***\n  *****\n *******\n*********\n *******\n  *****\n   ***\n    *\n'),
                             (-4, None),
                             (5, '  *\n ***\n*****\n ***\n  *\n'),
                             (-9, None),
                             (11, '     *\n    ***\n   *****\n  *******\n *********\n***********\n *********\n  *******\n   *****\n    ***\n     *\n'),
                             (7, '   *\n  ***\n *****\n*******\n *****\n  ***\n   *\n')])
def test_random_test_cases(a, b):
    assert diamond(a) == b
