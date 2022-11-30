import pytest
from functions import *

def test_initial_answer():
    assert initial_answer(['a','b','c','d'],[2,1,0,1]) == ['a','a','b','d']


    