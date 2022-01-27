import list_of_squares

def test_list_of_squares_control():
    assert list_of_squares.list_of_squares(1) == {1: 1}

def test_list_of_squares_4():
    assert list_of_squares.list_of_squares(4) == {1: 1, 2: 4, 3: 9, 4: 16}

def test_list_of_squares_10():
    assert list_of_squares.list_of_squares(10) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

def test_list_of_squares_7():
    assert list_of_squares.list_of_squares(7) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}

def test_list_of_squares_9():
    assert list_of_squares.list_of_squares(9) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

def test_list_of_squares_2():
    assert list_of_squares.list_of_squares(2) == {1: 1, 2: 4}

def test_list_of_squares_3():
    assert list_of_squares.list_of_squares(3) == {1: 1, 2: 4, 3: 9}

def test_list_of_squares_5():
    assert list_of_squares.list_of_squares(5) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

def test_length_dict():
    assert len(list_of_squares.list_of_squares(2))== 2
