import factorial

def test_factorial_control():
    assert factorial.fact(1) == 1

def test_factorial_2():
    assert factorial.fact(2) == 2

def test_factorial_3():
    assert factorial.fact(5) == 120
    
def test_factorial_0():
    assert factorial.fact(0) == 1