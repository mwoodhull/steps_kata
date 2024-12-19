from src.step import step

def test_x_and_y_are_the_same():

    input1 = 4
    input2 = 4
    output = step(input1, input2)

    assert output == 0

def test_x_and_y_are_one_apart():

    input1 = 11
    input2 = 12
    output = step(input1, input2)

    assert output == 1   

def test_x_and_y_that_are_two_apart():

    input1 = 11
    input2 = 13
    output = step(input1, input2)

    assert output == 2

def test_x_and_y_are_3_apart():

    input1 = 52
    input2 = 55
    output = step(input1, input2)

    assert output == 3

def test_x_and_y_are_more_than_3_apart():

    input1 = 52
    input2 = 57
    output = step(input1, input2)

    assert output == 4

    input1 = 53
    input2 = 57
    output = step(input1, input2)

    assert output == 3

    input1 = 51
    input2 = 57
    output = step(input1, input2)

    assert output == 5