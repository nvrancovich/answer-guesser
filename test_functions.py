import pytest
from functions import *

def test_initial_answer():
    assert initial_answer(['a','b','c','d'],[2,1,0,1]) == ['a','a','b','d']

def test_check_distributions():
    assert check_distribution([['a','undifined'],['a','undifined'],['a','undifined']], ['a','b','c'], [1,0,2]) == [-2, 0, 2]