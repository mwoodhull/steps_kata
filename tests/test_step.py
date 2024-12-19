from src.step import step

def test_x_and_y_that_are_two_apart():
    input1 = 11
    input2 = 13

    output = step(input1, input2)

    assert output == 2