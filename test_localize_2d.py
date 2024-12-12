import logging
import pytest
from localize_2d import localize, show

def compare_result(result_2d_array, expected_2d_array, tolerance):
    result = True
    for i in range(len(result_2d_array)):
        for j in range(len(result_2d_array[i])):
            if abs(result_2d_array[i][j] - expected_2d_array[i][j]) <= tolerance:
                continue
            else:
                logging.error(f"Result not within tolerance at : {i},{j}")
                logging.error(f"Result value : {result_2d_array[i][j]}, expected_value : {expected_2d_array[i][j]}")
                result = False
    return result


def test_1():
    expected_result = [[0.01105, 0.02464, 0.06799, 0.04472, 0.02465],
        [0.00715, 0.01017, 0.08696, 0.07988, 0.00935],
        [0.00739, 0.00894, 0.11272, 0.35350, 0.04065],
        [0.00910, 0.00715, 0.01434, 0.04313, 0.03642]]
    # (within a tolerance of +/- 0.001 for each entry)


    colors = [['R','G','G','R','R'],
            ['R','R','G','R','R'],
            ['R','R','G','G','R'],
            ['R','R','R','R','R']]
    measurements = ['G','G','G','G','G']
    motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]
    sensor_right = 0.7
    p_move = 0.8
    tolerance = 0.001

    assert compare_result( localize(colors,measurements,motions,sensor_right = sensor_right, p_move = p_move) , expected_result, tolerance), "Test failed"

def test_2():
    correct_answer = [[0.0, 0.0, 0.0],
     [0.0, 1.0, 0.0],
     [0.0, 0.0, 0.0]]

    colors = [['G', 'G', 'G'],
            ['G', 'R', 'G'],
            ['G', 'G', 'G']]
    measurements = ['R']
    motions = [[0,0]]
    sensor_right = 1.0
    p_move = 1.0
    tolerance = 0.001
    assert compare_result( localize(colors,measurements,motions,sensor_right = sensor_right, p_move = p_move) , correct_answer, tolerance), "Test failed"


def test_3():
    colors = [['G', 'G', 'G'],
            ['G', 'R', 'R'],
            ['G', 'G', 'G']]
    measurements = ['R']
    motions = [[0,0]]
    sensor_right = 1.0
    p_move = 1.0
    tolerance = 0.001
    correct_answer = [[0.0, 0.0, 0.0],
        [0.0, 0.5, 0.5],
        [0.0, 0.0, 0.0]]
    tolerance = 0.001
    assert compare_result( localize(colors,measurements,motions,sensor_right = sensor_right, p_move = p_move) , correct_answer, tolerance), "Test failed"

def test_4():
    colors = [['G', 'G', 'G'],
            ['G', 'R', 'R'],
            ['G', 'G', 'G']]
    measurements = ['R']
    motions = [[0,0]]
    sensor_right = 0.8
    p_move = 1.0
    correct_answer = [[0.06666666666, 0.06666666666, 0.06666666666],
        [0.06666666666, 0.26666666666, 0.26666666666],
        [0.06666666666, 0.06666666666, 0.06666666666]]
    tolerance = 0.001
    assert compare_result( localize(colors,measurements,motions,sensor_right = sensor_right, p_move = p_move) , correct_answer, tolerance), "Test failed"

def test_5():
    colors = [['G', 'G', 'G'],
            ['G', 'R', 'R'],
            ['G', 'G', 'G']]
    measurements = ['R', 'R']
    motions = [[0,0], [0,1]]
    sensor_right = 0.8
    p_move = 1.0
    correct_answer = [[0.03333333333, 0.03333333333, 0.03333333333],
        [0.13333333333, 0.13333333333, 0.53333333333],
        [0.03333333333, 0.03333333333, 0.03333333333]]
    tolerance = 0.001
    assert compare_result( localize(colors,measurements,motions,sensor_right = sensor_right, p_move = p_move) , correct_answer, tolerance), "Test failed"


def test_6():
    colors = [['G', 'G', 'G'],
            ['G', 'R', 'R'],
            ['G', 'G', 'G']]
    measurements = ['R', 'R']
    motions = [[0,0], [0,1]]
    sensor_right = 1.0
    p_move = 1.0
    correct_answer = [[0.0, 0.0, 0.0],
        [0.0, 0.0, 1.0],
        [0.0, 0.0, 0.0]]
    tolerance = 0.001
    assert compare_result( localize(colors,measurements,motions,sensor_right = sensor_right, p_move = p_move) , correct_answer, tolerance), "Test failed"

def test_7():
    colors = [['G', 'G', 'G'],
            ['G', 'R', 'R'],
            ['G', 'G', 'G']]
    measurements = ['R', 'R']
    motions = [[0,0], [0,1]]
    sensor_right = 0.8
    p_move = 0.5
    correct_answer = [[0.0289855072, 0.0289855072, 0.0289855072],
        [0.0724637681, 0.2898550724, 0.4637681159],
        [0.0289855072, 0.0289855072, 0.0289855072]]
    tolerance = 0.001
    assert compare_result( localize(colors,measurements,motions,sensor_right = sensor_right, p_move = p_move) , correct_answer, tolerance), "Test failed"

def test_8():
    colors = [['G', 'G', 'G'],
            ['G', 'R', 'R'],
            ['G', 'G', 'G']]
    measurements = ['R', 'R']
    motions = [[0,0], [0,1]]
    sensor_right = 1.0
    p_move = 0.5
    correct_answer = [[0.0, 0.0, 0.0],
        [0.0, 0.33333333, 0.66666666],
        [0.0, 0.0, 0.0]]
    tolerance = 0.001
    assert compare_result( localize(colors,measurements,motions,sensor_right = sensor_right, p_move = p_move) , correct_answer, tolerance), "Test failed"
