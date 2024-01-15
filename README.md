# evaluation2024

#NOM Prénom :
#RAMOND Nicolas
#Version :
#0.0.0
#Date :
#15/01/24

#Résultats des tests unitaires :
#
============================= test session starts =============================
platform win32 -- Python 3.11.7, pytest-7.4.4, pluggy-1.3.0
rootdir:
plugins: cov-4.1.0
collected 3 items

test\test_steve.py ...                                                   [100%]

============================== 3 passed in 0.01s ==============================
Finished running tests!
#
#
#
#
#
#
============================= test session starts =============================
platform win32 -- Python 3.11.7, pytest-7.4.4, pluggy-1.3.0
rootdir:
plugins: cov-4.1.0
collected 3 items

test\test_turing.py ..F                                                  [100%]

================================== FAILURES ===================================
_________________________________ test_somme __________________________________

    def test_somme():
>       assert somme(7, 1, 6)
E       assert False
E        +  where False = somme(7, 1, 6)

test\test_turing.py:16: AssertionError
=========================== short test summary info ===========================
FAILED test/test_turing.py::test_somme - assert False
========================= 1 failed, 2 passed in 0.07s =========================
Finished running tests!
